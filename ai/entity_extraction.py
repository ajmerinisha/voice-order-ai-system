import re

food_items = [
    "pizza",
    "burger",
    "dosa",
    "sandwich",
    "pasta",
    "coke",
    "biryani",
    "momos",
    "vadapav",
    "noodles",
    "fries",
    "coffee",
    "tea"
]

def extract_entities(text):

    text = text.lower()

    quantity = 1

    numbers = re.findall(r'\d+', text)

    if numbers:
        quantity = int(numbers[0])

    item_name = "unknown"

    for item in food_items:

        if item in text:
            item_name = item

    return {
        "item": item_name,
        "quantity": quantity,
        "restaurant": "Dominos"
    }