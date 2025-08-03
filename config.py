"""
Configuration settings for Smart Shopping Assistant.
All sensitive data should be stored in .env file.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STEEL_API_URL = os.getenv("STEEL_API_URL", "http://localhost:3000")
STEEL_API_KEY = os.getenv("STEEL_API_KEY")
USE_STEEL_API = os.getenv("USE_STEEL_API", "true").lower() == "true"

# Shopping targets - what to search for on each site
SHOPPING_TARGETS = {
    "Nike": {
        "url": "https://www.nike.com",
        "search_term": "Air Jordan basketball shoes",
        "language": "English"
    },
    "Lululemon": {
        "url": "https://shop.lululemon.com",
        "search_term": "women's leggings athletic",
        "language": "English"
    },
    "PaynGo": {
        "url": "https://www.payngo.co.il",
        "search_term": "טוסטר כלי מטבח למשק",
        "language": "Hebrew"
    }
}
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Steel Browser API Configuration
STEEL_API_URL = os.getenv("STEEL_BASE_URL")
STEEL_API_KEY = os.getenv("STEEL_API_KEY")
USE_STEEL_API = STEEL_API_URL and STEEL_API_KEY

# Shopping Targets
SHOPPING_TARGETS = {
    "Nike": {
        "category": "air_jordans",
        "url": "https://www.nike.com",
        "search_term": "Air Jordan basketball shoes",
        "language": "English"
    },
    "Lululemon": {
        "category": "leggings",
        "url": "https://shop.lululemon.com",
        "search_term": "women's leggings athletic",
        "language": "English"
    },
    "PaynGo": {
        "category": "toasters",
        "url": "https://www.payngo.co.il",
        "search_term": "טוסטר מטבח כלי חשמל",
        "language": "Hebrew"
    }
}
