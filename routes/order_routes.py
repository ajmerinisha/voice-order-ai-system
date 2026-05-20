from flask import Blueprint, request, jsonify

from services.order_service import save_order

order_bp = Blueprint("order_bp", __name__)


@order_bp.route("/place-order", methods=["POST"])
def place_order():

    data = request.json

    save_order(data)

    return jsonify({
        "message": "Order placed successfully",
        "order": data
    })