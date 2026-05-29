def validate_audio(audio):
    
    if audio.filename == "":
        return False

    return True


def validate_order(data):

    if 'item' not in data:
        return False

    if 'quantity' not in data:
        return False

    return True