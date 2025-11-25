import sqlite3

# create database file
conn = sqlite3.connect("solutions.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS solutions (
    disease TEXT,
    lang TEXT,
    organic_solution TEXT,
    ingredients TEXT
)
""")

conn.commit()
conn.close()
print("Database created successfully!")
