prices = {
    "espresso": 3.25,
    "frappuccino": 6.45,
    "americano": 3.95,
    "latte": 5.25,
    "cold brew": 4.95,
    "matcha": 5.75,
    "croissant": 3.95,
    "cake pop": 3.25,
    "ham sandwich": 7.45,
    "bacon sandwich": 7.95
}

def get_price(item):
    return prices.get(item)

def show_prices():
    print("=== MENU ===")
    for item, price in prices.items():
        print(f"{item}: ${price:.2f}")