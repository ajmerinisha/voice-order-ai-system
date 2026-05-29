import re

def extract_entities(text):

    text = text.lower()

    # Default values
    quantity = 1
    item = "unknown"
    restaurant = "unknown"

    # -------------------------
    # QUANTITY DETECTION
    # -------------------------
    quantity_match = re.search(r'\d+', text)

    if quantity_match:
        quantity = int(quantity_match.group())

    # -------------------------
    # FOOD ITEM DETECTION
    # -------------------------
    food_items = [
        "dosa",
        "pizza",
        "burger",
        "pasta",
        "sandwich",
        "idli",
        "fries"
    ]

    for food in food_items:
        if food in text:
            item = food
            break

    # -------------------------
    # RESTAURANT DETECTION
    # -------------------------
    restaurants = [
        "madras cafe",
        "dominos",
        "kfc",
        "subway",
        "pizza hut"
    ]

    for r in restaurants:
        if r in text:
            restaurant = r
            break

    # -------------------------
    # DEBUG OUTPUT
    # -------------------------
    print("TEXT:", text)
    print("ITEM:", item)
    print("QUANTITY:", quantity)
    print("RESTAURANT:", restaurant)

    return {
        "item": item,
        "quantity": quantity,
        "restaurant": restaurant
    }