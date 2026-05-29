from models.database import connect_db

def create_user(name, email, language):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        language TEXT
    )
    ''')

    cursor.execute(
        "INSERT INTO users(name,email,language) VALUES(?,?,?)",
        (name, email, language)
    )

    conn.commit()

    conn.close()