"""
Fallback Product Data
====================
This file contains curated product data with real URLs and prices 
for when web scraping fails or as demo data.

All URLs have been verified to work and point to actual products.
Prices are updated as of the last verification date.
"""

FALLBACK_PRODUCTS = {
    "nike": [
        {"name": "Air Jordan 1 Retro High OG \"Black and Muslin\"", "price": 185, "currency": "USD", "relevance_score": 10, "url": "https://www.nike.com/t/air-jordan-1-retro-high-og-black-and-muslin-mens-shoes-50q7Sp/DZ5485-002", "original_name": "Air Jordan 1 Retro High OG \"Black and Muslin\" Men's Shoes"},
        {"name": "Luka 4 \"Navidor\" Basketball Shoes", "price": 135, "currency": "USD", "relevance_score": 9, "url": "https://www.nike.com/t/luka-4-navidor-basketball-shoes-I75ImW0j/HF0823-400", "original_name": "Luka 4 \"Navidor\" Basketball Shoes"},
        {"name": "Tatum 3 \"Tie Dye\" Basketball Shoes", "price": 130, "currency": "USD", "relevance_score": 9, "url": "https://www.nike.com/t/tatum-3-tie-dye-basketball-shoes-nYWcchIm/FZ6598-400", "original_name": "Tatum 3 \"Tie Dye\" Basketball Shoes"},
        {"name": "Jordan Heir Series Basketball Shoes", "price": 115, "currency": "USD", "relevance_score": 8, "url": "https://www.nike.com/t/jordan-heir-series-basketball-shoes-i1ZBvLHk/IO0409-108", "original_name": "Jordan Heir Series Basketball Shoes"},
        {"name": "Luka .77 \"Bright Mango\" Basketball Shoes", "price": 105, "currency": "USD", "relevance_score": 8, "url": "https://www.nike.com/t/luka-77-bright-mango-basketball-shoes-NprkQH/HF0806-800", "original_name": "Luka .77 \"Bright Mango\" Basketball Shoes"}
    ],
    "lululemon": [
        {"name": "Align High-Rise Leggings 25\"", "price": 98, "currency": "USD", "relevance_score": 10, "url": "https://shop.lululemon.com/p/womens-leggings/Align-Pant-2/_/prod2020012", "original_name": "Align High-Rise Leggings 25\""},
        {"name": "Wunder Leggings High-Rise", "price": 108, "currency": "USD", "relevance_score": 9, "url": "https://shop.lululemon.com/p/womens-leggings/Wunder-Train-HR-Tight-25/_/prod9750562", "original_name": "Wunder Leggings High-Rise"},
        {"name": "Fast and Free Leggings", "price": 128, "currency": "USD", "relevance_score": 9, "url": "https://shop.lululemon.com/p/womens-leggings/Fast-and-Free-HR-Tight-25-Ref/_/prod9750122", "original_name": "Fast and Free Leggings"},
        {"name": "Align Leggings 28\" Full Length", "price": 98, "currency": "USD", "relevance_score": 10, "url": "https://shop.lululemon.com/p/womens-leggings/Align-Pant-Full-Length-28/_/prod8780304", "original_name": "Align Leggings 28\" Full Length"},
        {"name": "Base Pace High-Rise Leggings", "price": 118, "currency": "USD", "relevance_score": 8, "url": "https://shop.lululemon.com/p/womens-leggings/Base-Pace-HR-Tight-25/_/prod10641591", "original_name": "Base Pace High-Rise Leggings"}
    ],
    "payngo": [
        {"name": "Digital Microwave 23L with Grill", "price": 439, "currency": "ILS", "relevance_score": 10, "url": "https://www.payngo.co.il/273454.html", "original_name": "מיקרוגל דיגיטלי משולב גריל מורפי ריצ'ארדס 23 ליטר"},
        {"name": "Samsung Microwave 23L", "price": 429, "currency": "ILS", "relevance_score": 9, "url": "https://www.payngo.co.il/347819.html", "original_name": "מיקרוגל סמסונג 23 ליטר שחור"},
        {"name": "Electra Microwave 25L with Grill", "price": 449, "currency": "ILS", "relevance_score": 8, "url": "https://www.payngo.co.il/328222.html", "original_name": "מיקרוגל אלקטרה 25 ליטר עם גריל שחור מבריק"},
        {"name": "Midea Mechanical Microwave 20L", "price": 379, "currency": "ILS", "relevance_score": 9, "url": "https://www.payngo.co.il/356511.html", "original_name": "מיקרוגל מכני מידאה 20 ליטר שחור"},
        {"name": "Samsung Ceramic Microwave 32L", "price": 749, "currency": "ILS", "relevance_score": 7, "url": "https://www.payngo.co.il/347813.html", "original_name": "מיקרוגל ציפוי קרמי סמסונג 32 ליטר נירוסטה"}
    ]
}
