import sqlite3

conn = sqlite3.connect("store.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

try:
    with conn:
        cur.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Geetha", "geetha@gmail.com"))
        cur.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Mahi", "ms@gmail.com"))
    print("Inserted 2 customers in a transaction.")
except Exception as e:
    print("Transaction failed:", e)


