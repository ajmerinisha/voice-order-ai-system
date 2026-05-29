from models.database import connect_db

def save_voice_session(transcript, confidence):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS voice_sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transcript TEXT,
        confidence REAL
    )
    ''')

    cursor.execute(
        "INSERT INTO voice_sessions(transcript, confidence) VALUES (?, ?)",
        (transcript, confidence)
    )

    conn.commit()

    conn.close()