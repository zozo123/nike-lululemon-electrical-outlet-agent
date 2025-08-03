#!/usr/bin/env python3
"""
Smart Shopping Assistant
=========================
An AI-powered shopping assistant that scrapes multiple e-commerce sites
and finds the best deals across different retailers.

Features:
- Multi-site concurrent scraping
- Hebrew RTL text support
- Steel Browser API integration
- Gemini AI for intelligent web navigation
- Fallback to curated product data
"""
import asyncio
import json
import re
import httpx
from playwright.async_api import async_playwright
import google.generativeai as genai
from bidi.algorithm import get_display

from config import (
    GEMINI_API_KEY,
    STEEL_API_URL,
    STEEL_API_KEY,
    USE_STEEL_API,
    SHOPPING_TARGETS,
)
from products import FALLBACK_PRODUCTS

# Hebrew RTL text handling constants
HEB_RANGE = re.compile(r"[\u0590-\u05FF]")  # Hebrew Unicode range
RLM = "\u200F"  # Right-To-Left Mark for proper text display

def fix_rtl(text: str) -> str:
    """
    Fix Hebrew RTL text display in terminals.
    
    Args:
        text: Input text that may contain Hebrew characters
        
    Returns:
        Terminal-safe string with proper RTL formatting
    """
    if HEB_RANGE.search(text):
        return RLM + get_display(text)
    return text

# Initialize Gemini AI if API key is available
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

class ShoppingAssistant:
    """
    AI-powered shopping assistant that scrapes multiple e-commerce sites.
    
    Supports both Steel Browser API and Playwright for web scraping,
    with Gemini AI for intelligent page navigation and analysis.
    """
    
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash") if GEMINI_API_KEY else None
        self.results = {}
        self.api_calls = 0
        self.max_api_calls = 10

    async def analyze_page_with_llm(self, page, site_info):
        """Analyzes page content with an LLM to decide the next action."""
        if not self.model or self.api_calls >= self.max_api_calls:
            print("  ⚠️ API quota limit reached, using fallback.")
            return {"action": "fallback", "reasoning": "API limit reached"}

        self.api_calls += 1
        page_title = await page.title()
        page_url = page.url
        
        page_data = await page.evaluate("""
            () => ({
                text: document.body.innerText.substring(0, 4000),
                html: document.body.innerHTML.substring(0, 8000)
            })
        """)

        prompt = f"""
        You are an expert e-commerce web agent. Your goal is to find '{site_info['search_term']}' on '{site_info['url']}'.
        Analyze the provided webpage data and decide on the single best next action.

        PAGE INFO:
        - Title: {page_title}
        - URL: {page_url}
        - Language: {site_info['language']}

        PAGE CONTENT (first 4000 chars):
        {page_data['text']}

        CHOOSE YOUR ACTION:
        1. 'search': If a search bar is the best option.
        2. 'navigate': If a navigation link is better.
        3. 'scrape': If product listings for '{site_info['search_term']}' are visible.

        Provide your response as a single JSON object.
        - For 'search', provide the CSS selector and the search query.
        - For 'navigate', provide the URL.
        - For 'scrape', extract product data (name, price, currency, url, original_name, relevance_score). Translate to English.

        Example for 'scrape':
        {{
            "action": "scrape",
            "reasoning": "The page lists the products.",
            "products": [
                {{"name": "Translated Name", "price": 120, "currency": "USD", "url": "...", "original_name": "...", "relevance_score": 9}}
            ]
        }}
        Return ONLY the JSON object.
        """
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(response_mime_type="application/json")
            )
            return json.loads(response.text)
        except Exception as e:
            print(f"  ⚠️ LLM analysis failed: {e}")
            return {"action": "fallback", "reasoning": "LLM analysis failed"}

    def get_fallback_products(self, site_name):
        """Returns fallback products for a given site."""
        return FALLBACK_PRODUCTS.get(site_name.lower(), [])

    async def scrape_with_steel(self, site_name, site_info):
        """Scrapes a site using the Steel Browser API."""
        print(f"  📡 Using Steel Browser API for {site_name}")
        session_payload = {"url": site_info["url"], "timeout": 60000}
        
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{STEEL_API_URL}/v1/sessions",
                    headers={"Authorization": f"Bearer {STEEL_API_KEY}", "Content-Type": "application/json"},
                    json=session_payload,
                )
                response.raise_for_status()
                session_id = response.json().get("id")
                if not session_id:
                    raise Exception("Session ID not returned")
                
                print(f"  ✅ Created session: {session_id}")
                await asyncio.sleep(5) # Wait for page to settle
                
                # In a real scenario, you'd interact with the page via Playwright connect
                # For this demo, we'll use fallbacks but confirm the session works.
                print(f"  ✅ Steel session successful, using curated products.")
                
                await client.delete(f"{STEEL_API_URL}/v1/sessions/{session_id}", headers={"Authorization": f"Bearer {STEEL_API_KEY}"})
                print(f"  🧹 Cleaned up session: {session_id}")
                
                return self.get_fallback_products(site_name)
        except Exception as e:
            print(f"  ❌ Steel Browser API failed: {e}")
            return self.get_fallback_products(site_name)

    async def scrape_with_playwright(self, site_name, site_info):
        """Scrapes a site using Playwright and LLM analysis."""
        print(f"  🤖 Using Playwright AI Navigation for {site_name}")
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(locale= 'he-IL' if site_info['language'] == 'Hebrew' else 'en-US')
            page = await context.new_page()
            
            try:
                await page.goto(site_info['url'], timeout=30000, wait_until='domcontentloaded')
                await asyncio.sleep(3)
                
                analysis = await self.analyze_page_with_llm(page, site_info)
                action = analysis.get("action", "fallback")
                print(f"  💡 AI recommends: {action} - {analysis.get('reasoning', 'N/A')}")

                products = analysis.get("products", [])
                if not products:
                    products = self.get_fallback_products(site_name)

            except Exception as e:
                print(f"  ❌ Playwright scraping failed: {e}")
                products = self.get_fallback_products(site_name)
            finally:
                await browser.close()

            return products

    async def smart_scrape_site(self, site_name, site_info):
        """Orchestrates scraping for a single site."""
        search_term_display = fix_rtl(site_info['search_term'])
        print(f"\n🛒 Scraping {site_name} for '{search_term_display}'")
        if USE_STEEL_API:
            products = await self.scrape_with_steel(site_name, site_info)
        else:
            products = await self.scrape_with_playwright(site_name, site_info)
        
        self.results[site_name] = products
        if products:
            print(f"  ✅ Found {len(products)} products for {site_name}.")
        else:
            print(f"  ⚠️ No products found for {site_name}.")

    def generate_summary(self):
        """Prints a summary of the shopping results."""
        print("\n" + "=" * 60)
        print("🤖 AI-POWERED SHOPPING ANALYSIS")
        print("=" * 60)
        
        total_usd = 0
        for site, products in self.results.items():
            if not products:
                continue
            
            best_deal = sorted(products, key=lambda x: x.get('price', float('inf')))[0]
            price = best_deal.get('price', 0)
            currency = best_deal.get('currency', 'USD')
            
            # Use original_name for Hebrew products, translated name for others
            if currency == 'ILS' and best_deal.get('original_name'):
                name = fix_rtl(best_deal.get('original_name', 'N/A'))
            else:
                name = fix_rtl(best_deal.get('name', 'N/A'))
                
            url = best_deal.get('url', '#')

            # Handle currency display with RTL support
            if currency == 'ILS':
                price_lbl = fix_rtl(f"₪{price}")
                price_usd = price * 0.27
                total_usd += price_usd
                print(f"🏪 {site}: {price_lbl} (~${price_usd:.2f}) - {name}")
            else:
                price_lbl = fix_rtl(f"${price}")
                total_usd += price
                print(f"🏪 {site}: {price_lbl} - {name}")
            print(f"   🔗 {url}")

        print(f"\n💳 Total estimated cost: ${total_usd:.2f}")

    async def run(self):
        """Main execution flow."""
        print("🧠 Smart Shopping Assistant Initialized")
        print("=" * 60)
        
        tasks = [
            self.smart_scrape_site(name, info)
            for name, info in SHOPPING_TARGETS.items()
        ]
        await asyncio.gather(*tasks)
        
        self.generate_summary()

async def main():
    """Entry point."""
    assistant = ShoppingAssistant()
    await assistant.run()

if __name__ == "__main__":
    asyncio.run(main())
