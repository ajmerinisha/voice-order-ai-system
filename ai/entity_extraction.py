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

    # Quantity Detection
    quantity = 1

    numbers = re.findall(r'\d+', text)

    if numbers:
        quantity = int(numbers[0])

    # Food Item Detection
    item_name = "unknown"

    for item in food_items:

        if item in text:
            item_name = item
            break

    # Restaurant Detection
    restaurant = "Not Specified"

    if "from" in text:

        parts = text.split("from")

        if len(parts) > 1:
            restaurant = parts[1].strip()

    return {
        "item": item_name,
        "quantity": quantity,
        "restaurant": restaurant
    }