
from flask import Blueprint, render_template
import json
import os

order_bp = Blueprint("order_bp", __name__)


@order_bp.route("/cart")
def cart():

    if not os.path.exists("database/cart.json"):

        with open("database/cart.json", "w") as f:
            json.dump([], f)

    with open("database/cart.json", "r") as f:

        cart_items = json.load(f)

    return render_template(
        "cart.html",
        cart_items=cart_items
    )


@order_bp.route("/clear-cart")
def clear_cart():

    with open("database/cart.json", "w") as f:

        json.dump([], f)

    return render_template(
        "cart.html",
        cart_items=[]
    )

