import sqlite3

def create_tables():
    conn = sqlite3.connect("database/orders.db")
    cursor = conn.cursor()

    # Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant TEXT,
        item TEXT,
        quantity INTEGER,
        status TEXT
    )
    """)

    # History Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        restaurant TEXT,
        item TEXT,
        quantity INTEGER,
        order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Cart Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()

    print("Tables created successfully!")

create_tables()