"""
Restaurant Knowledge Base - Menu, Information, and Data
"""

MENU_DATA = {
    "Appetizers": [
        {
            "name": "Bruschetta Trio",
            "price": 12.99,
            "description": "Three varieties: classic tomato basil, mushroom truffle, and roasted pepper",
            "dietary": ["vegetarian"],
            "popular": True
        },
        {
            "name": "Calamari Fritti",
            "price": 14.99,
            "description": "Crispy fried calamari with lemon aioli and marinara",
            "dietary": [],
            "popular": True
        },
        {
            "name": "Caprese Salad",
            "price": 11.99,
            "description": "Fresh mozzarella, heirloom tomatoes, basil, balsamic glaze",
            "dietary": ["vegetarian", "gluten-free"],
            "popular": False
        },
        {
            "name": "Stuffed Mushrooms",
            "price": 10.99,
            "description": "Portobello mushrooms stuffed with herbs, cheese, and breadcrumbs",
            "dietary": ["vegetarian"],
            "popular": False
        }
    ],
    "Main Courses": [
        {
            "name": "Osso Buco",
            "price": 32.99,
            "description": "Braised veal shanks with saffron risotto and gremolata",
            "dietary": ["gluten-free"],
            "popular": True,
            "chef_special": True
        },
        {
            "name": "Seafood Linguine",
            "price": 28.99,
            "description": "Fresh lobster, shrimp, mussels in white wine garlic sauce",
            "dietary": [],
            "popular": True
        },
        {
            "name": "Chicken Marsala",
            "price": 24.99,
            "description": "Pan-seared chicken breast with mushroom marsala wine sauce",
            "dietary": ["gluten-free"],
            "popular": True
        },
        {
            "name": "Eggplant Parmigiana",
            "price": 19.99,
            "description": "Breaded eggplant layered with marinara, mozzarella, and parmesan",
            "dietary": ["vegetarian"],
            "popular": False
        },
        {
            "name": "Grilled Salmon",
            "price": 26.99,
            "description": "Atlantic salmon with lemon butter, asparagus, and roasted potatoes",
            "dietary": ["gluten-free"],
            "popular": True
        },
        {
            "name": "Ribeye Steak",
            "price": 38.99,
            "description": "14oz prime ribeye with herb butter and seasonal vegetables",
            "dietary": ["gluten-free"],
            "popular": True,
            "chef_special": True
        },
        {
            "name": "Mushroom Risotto",
            "price": 21.99,
            "description": "Creamy arborio rice with wild mushrooms and truffle oil",
            "dietary": ["vegetarian", "gluten-free"],
            "popular": False
        }
    ],
    "Pasta": [
        {
            "name": "Spaghetti Carbonara",
            "price": 18.99,
            "description": "Classic Roman pasta with pancetta, egg, pecorino romano",
            "dietary": [],
            "popular": True
        },
        {
            "name": "Fettuccine Alfredo",
            "price": 17.99,
            "description": "Rich and creamy parmesan sauce with fettuccine",
            "dietary": ["vegetarian"],
            "popular": True
        },
        {
            "name": "Penne Arrabbiata",
            "price": 16.99,
            "description": "Spicy tomato sauce with garlic and red chili flakes",
            "dietary": ["vegan"],
            "popular": False
        },
        {
            "name": "Lobster Ravioli",
            "price": 29.99,
            "description": "Handmade ravioli filled with lobster in pink vodka sauce",
            "dietary": [],
            "popular": True,
            "chef_special": True
        }
    ],
    "Desserts": [
        {
            "name": "Tiramisu",
            "price": 8.99,
            "description": "Classic Italian dessert with espresso-soaked ladyfingers and mascarpone",
            "dietary": ["vegetarian"],
            "popular": True
        },
        {
            "name": "Panna Cotta",
            "price": 7.99,
            "description": "Vanilla bean panna cotta with berry compote",
            "dietary": ["vegetarian", "gluten-free"],
            "popular": False
        },
        {
            "name": "Chocolate Lava Cake",
            "price": 9.99,
            "description": "Warm chocolate cake with molten center, vanilla gelato",
            "dietary": ["vegetarian"],
            "popular": True
        },
        {
            "name": "Cannoli",
            "price": 7.99,
            "description": "Crispy pastry shells filled with sweet ricotta and chocolate chips",
            "dietary": ["vegetarian"],
            "popular": True
        }
    ],
    "Beverages": [
        {
            "name": "Italian Espresso",
            "price": 3.99,
            "description": "Rich and bold espresso shot",
            "dietary": ["vegan", "gluten-free"],
            "popular": True
        },
        {
            "name": "Cappuccino",
            "price": 4.99,
            "description": "Espresso with steamed milk and foam",
            "dietary": ["vegetarian", "gluten-free"],
            "popular": True
        },
        {
            "name": "Fresh Lemonade",
            "price": 3.99,
            "description": "House-made lemonade with mint",
            "dietary": ["vegan", "gluten-free"],
            "popular": False
        },
        {
            "name": "San Pellegrino",
            "price": 4.99,
            "description": "Sparkling mineral water",
            "dietary": ["vegan", "gluten-free"],
            "popular": False
        }
    ]
}

WINE_LIST = {
    "Red Wines": [
        {"name": "Chianti Classico", "price": 45.00, "region": "Tuscany, Italy"},
        {"name": "Barolo", "price": 85.00, "region": "Piedmont, Italy"},
        {"name": "Cabernet Sauvignon", "price": 55.00, "region": "Napa Valley, USA"}
    ],
    "White Wines": [
        {"name": "Pinot Grigio", "price": 38.00, "region": "Veneto, Italy"},
        {"name": "Chardonnay", "price": 48.00, "region": "Burgundy, France"},
        {"name": "Sauvignon Blanc", "price": 42.00, "region": "Marlborough, NZ"}
    ]
}

SPECIAL_OFFERS = [
    {
        "name": "Happy Hour",
        "description": "50% off appetizers and select drinks",
        "time": "Monday-Friday, 4:00 PM - 6:00 PM"
    },
    {
        "name": "Sunday Brunch",
        "description": "Special brunch menu with bottomless mimosas",
        "time": "Sunday, 10:00 AM - 2:00 PM",
        "price": "$29.99 per person"
    },
    {
        "name": "Chef's Tasting Menu",
        "description": "5-course tasting menu with wine pairing",
        "time": "Available daily",
        "price": "$89.99 per person"
    }
]

DIETARY_INFO = {
    "vegetarian": "We offer multiple vegetarian options across all categories",
    "vegan": "Vegan options available, please ask your server for modifications",
    "gluten-free": "Gluten-free pasta and bread available upon request",
    "allergies": "Please inform your server of any allergies. We take all precautions seriously."
}

CHEF_RECOMMENDATIONS = [
    "Osso Buco - Our signature dish, slow-braised to perfection",
    "Lobster Ravioli - Handmade daily by our pasta chef",
    "Ribeye Steak - Premium cut, aged 28 days",
    "Tiramisu - Made with our secret family recipe"
]

def get_full_menu_text():
    """Generate formatted menu text for AI context"""
    menu_text = "BELLA VISTA RESTAURANT MENU\n\n"
    
    for category, items in MENU_DATA.items():
        menu_text += f"\n{category.upper()}\n" + "="*50 + "\n"
        for item in items:
            menu_text += f"\n{item['name']} - ${item['price']}\n"
            menu_text += f"  {item['description']}\n"
            if item.get('dietary'):
                menu_text += f"  Dietary: {', '.join(item['dietary'])}\n"
            if item.get('popular'):
                menu_text += "  ⭐ Popular Choice\n"
            if item.get('chef_special'):
                menu_text += "  👨‍🍳 Chef's Special\n"
    
    return menu_text

def search_menu(query):
    """Search menu items by name or description"""
    query = query.lower()
    results = []
    
    for category, items in MENU_DATA.items():
        for item in items:
            if (query in item['name'].lower() or 
                query in item['description'].lower() or
                query in category.lower()):
                results.append({**item, "category": category})
    
    return results

def get_items_by_dietary(dietary_type):
    """Get menu items by dietary restriction"""
    results = []
    
    for category, items in MENU_DATA.items():
        for item in items:
            if dietary_type.lower() in [d.lower() for d in item.get('dietary', [])]:
                results.append({**item, "category": category})
    
    return results

def get_popular_items():
    """Get all popular menu items"""
    results = []
    
    for category, items in MENU_DATA.items():
        for item in items:
            if item.get('popular'):
                results.append({**item, "category": category})
    
    return results
