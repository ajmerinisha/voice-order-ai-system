from ai.intent_detection import detect_intent

text = "2 dosa order karna hai"

intent = detect_intent(text)

print("Intent:", intent)