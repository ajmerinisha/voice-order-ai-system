import sqlite3

conn = sqlite3.connect("database/orders.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM cart")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()