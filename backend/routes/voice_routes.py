from flask import Blueprint, request, jsonify
import os
import json

from ai.speech_to_text import convert_audio_to_text
from ai.intent_detection import detect_intent
from ai.entity_extraction import extract_entities

voice_bp = Blueprint("voice_bp", __name__)

@voice_bp.route("/upload-audio", methods=["POST"])
def upload_audio():

    if "audio" not in request.files:

        return jsonify({
            "error": "No audio uploaded"
        })

    audio = request.files["audio"]

    filepath = os.path.join(
        "uploads/audio",
        audio.filename
    )

    audio.save(filepath)

    text = convert_audio_to_text(filepath)

    intent = detect_intent(text)

    # REORDER FEATURE
    if intent == "reorder":

        try:

            with open("database/orders.json", "r") as f:

                orders = json.load(f)

            last_order = orders[-1]

            return jsonify({
                "transcript": text,
                "intent": intent,
                "entities": last_order
            })

        except:

            return jsonify({
                "transcript": text,
                "intent": intent,
                "entities": {
                    "item": "No previous order",
                    "quantity": 0
                }
            })

    entities = extract_entities(text)

    return jsonify({
        "transcript": text,
        "intent": intent,
        "entities": entities
    })