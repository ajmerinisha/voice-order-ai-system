import sqlite3

def connect_db():

    conn = sqlite3.connect("database/orders.db")

    return conn


def create_tables():

    conn = connect_db()

    cursor = conn.cursor()

    # Orders Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity INTEGER,
        restaurant TEXT,
        status TEXT
    )
    ''')

    # Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        language TEXT
    )
    ''')

    # Voice Sessions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS voice_sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transcript TEXT,
        confidence REAL
    )
    ''')

    conn.commit()

    conn.close()