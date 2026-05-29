def detect_intent(text):
    
    text = text.lower()

    if "cancel" in text:
        return "cancel_order"

    elif "repeat" in text:
        return "reorder"

    elif "same order" in text:
        return "reorder"

    elif "previous order" in text:
        return "reorder"

    elif "again" in text:
        return "reorder"

    elif "add" in text:
        return "modify_order"

    elif "menu" in text:
        return "menu_details"

    else:
        return "place_order"