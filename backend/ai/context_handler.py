from models.database import connect_db

def get_last_restaurant():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT restaurant FROM orders ORDER BY id DESC LIMIT 1"
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "Dominos"