import sqlite3

def add_to_cart(item, quantity):

    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cart (item, quantity) VALUES (?, ?)",
        (item, quantity)
    )

    conn.commit()
    conn.close()

    print("Item added to cart!")