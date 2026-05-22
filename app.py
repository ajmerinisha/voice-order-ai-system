from flask import Flask, render_template, request
import sqlite3

from ai.intent_detection import detect_intent
from ai.entity_extraction import extract_entities
from routes.cart_routes import add_to_cart

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():

    return render_template("index.html")


# PROCESS ORDER
@app.route("/process", methods=["POST"])
def process_order():

    user_text = request.form["text"]

    # Intent Detection
    intent = detect_intent(user_text)

    # Entity Extraction
    entities = extract_entities(user_text)

    item = entities["item"]
    quantity = entities["quantity"]
    restaurant = entities["restaurant"]

    # Add To Cart
    add_to_cart(item, quantity)

    # Save To History Table
    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history
        (restaurant, item, quantity)
        VALUES (?, ?, ?)
        """,
        (restaurant, item, quantity)
    )

    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        transcript=user_text,
        intent=intent,
        item=item,
        quantity=quantity,
        restaurant=restaurant
    )


# VIEW CART
@app.route("/cart")
def view_cart():

    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cart")

    cart_items = cursor.fetchall()

    conn.close()

    return render_template(
        "cart.html",
        cart_items=cart_items
    )


# ORDER HISTORY
@app.route("/history")
def order_history():

    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history")

    history_items = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        history_items=history_items
    )


# CLEAR CART
@app.route("/clear_cart")
def clear_cart():

    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cart")

    conn.commit()
    conn.close()

    return render_template(
        "cart.html",
        cart_items=[]
    )


# CLEAR HISTORY
@app.route("/clear-history")
def clear_history():

    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history")

    conn.commit()
    conn.close()

    return "Order history cleared successfully!"


# REPEAT LAST ORDER
@app.route("/repeat_order")
def repeat_order():

    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT restaurant, item, quantity
        FROM history
        ORDER BY id DESC
        LIMIT 1
        """
    )

    last_order = cursor.fetchone()

    if last_order:

        restaurant = last_order[0]
        item = last_order[1]
        quantity = last_order[2]

        # Add again to cart
        cursor.execute(
            """
            INSERT INTO cart (item, quantity)
            VALUES (?, ?)
            """,
            (item, quantity)
        )

        conn.commit()

    conn.close()

    return render_template(
        "index.html",
        transcript="Repeat Last Order",
        intent="reorder",
        item=item if last_order else "None",
        quantity=quantity if last_order else 0,
        restaurant=restaurant if last_order else "None"
    )


if __name__ == "__main__":
    app.run(debug=True)