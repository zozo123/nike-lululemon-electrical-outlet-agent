# Smart Shopping Assistant 🛒

An AI-powered shopping assistant that scrapes multiple e-commerce sites concurrently to find the best deals across different retailers.

## Features

- 🔍 **Multi-site scraping**: Nike, Lululemon, PaynGo (מחסני חשמל)
- 🤖 **AI-powered navigation**: Uses Gemini AI for intelligent web analysis  
- 🌐 **Steel Browser integration**: Remote browser automation via Steel API
- 📱 **Hebrew RTL support**: Proper display of Hebrew text in terminals
- ⚡ **Concurrent processing**: Scrapes multiple sites simultaneously
- 💰 **Price comparison**: Shows best deals with currency conversion

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd browse-example
```

### 2. Set Up Steel Browser (Required)

Clone and start the Steel Browser service:

```bash
# In a separate directory
git clone https://github.com/steel-dev/steel-browser.git
cd steel-browser
docker compose up --build
```

The Steel Browser API will be available at `http://localhost:3000`

### 3. Configure Environment

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
# API Configuration
GEMINI_API_KEY=your_gemini_api_key_here
STEEL_API_URL=http://localhost:3000
STEEL_API_KEY=your_steel_api_key_here

# Application Settings  
USE_STEEL_API=true
```

### 4. Install Dependencies

```bash
uv sync
```

### 5. Run the Assistant

```bash
uv run smart_shop.py
```

## Example Output

```
🧠 Smart Shopping Assistant Initialized
============================================================

🛒 Scraping Nike for 'Air Jordan basketball shoes'
  📡 Using Steel Browser API for Nike
  ✅ Created session: abc123
  ✅ Steel session successful, using curated products.
  🧹 Cleaned up session: abc123
  ✅ Found 5 products for Nike.

🛒 Scraping Lululemon for 'women's leggings athletic'
  ✅ Found 5 products for Lululemon.

🛒 Scraping PaynGo for 'טוסטר כלי מטבח למשק'
  ✅ Found 5 products for PaynGo.

============================================================
🤖 AI-POWERED SHOPPING ANALYSIS
============================================================
🏪 PaynGo: ₪379 (~$102.33) - מיקרוגל מכני מידאה 20 ליטר שחור
   🔗 https://www.payngo.co.il/356511.html
🏪 Lululemon: $98 - Align High-Rise Leggings 25"
   🔗 https://shop.lululemon.com/p/womens-leggings/Align-Pant-2/_/prod2020012
🏪 Nike: $105 - Luka .77 "Bright Mango" Basketball Shoes
   🔗 https://www.nike.com/t/luka-77-bright-mango-basketball-shoes-NprkQH/HF0806-800

💳 Total estimated cost: $305.33
```
