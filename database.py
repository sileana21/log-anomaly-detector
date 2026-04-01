import sqlite3


conn = sqlite3.connect("alerts.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    user TEXT,
    severity TEXT
)
""")


def insert_alert(alert):

    cursor.execute(
        "INSERT INTO alerts (type, user, severity) VALUES (?, ?, ?)",
        (alert["type"], alert["user"], alert["severity"])
    )

    conn.commit()


def get_all_alerts():

    cursor.execute("SELECT type, user, severity FROM alerts")

    rows = cursor.fetchall()

    alerts = []

    for row in rows:

        alerts.append({
            "type": row[0],
            "user": row[1],
            "severity": row[2]
        })

    return alerts