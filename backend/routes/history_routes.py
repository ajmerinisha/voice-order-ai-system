from flask import Blueprint, render_template
import json
import os

history_bp = Blueprint("history_bp", __name__)


@history_bp.route("/history")
def history():

    if not os.path.exists("database/orders.json"):

        with open("database/orders.json", "w") as f:
            json.dump([], f)

    with open("database/orders.json", "r") as f:

        orders = json.load(f)

    return render_template(
        "history.html",
        orders=orders
    )


@history_bp.route("/clear-history")
def clear_history():

    with open("database/orders.json", "w") as f:

        json.dump([], f)

    return render_template(
        "history.html",
        orders=[]
    )

