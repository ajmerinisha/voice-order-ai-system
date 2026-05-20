from flask import Blueprint, jsonify

from services.order_service import get_all_orders

history_bp = Blueprint("history_bp", __name__)


@history_bp.route("/history", methods=["GET"])
def get_history():

    orders = get_all_orders()

    return jsonify({
        "history": orders
    })