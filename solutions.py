import sqlite3

def get_solution(disease_name, lang="en"):
    """
    Fetch organic solutions from the database based on disease and language.
    """

    # Connect to SQLite database
    conn = sqlite3.connect("solutions.db")
    cur = conn.cursor()

    # Query the database
    cur.execute("""
        SELECT organic_solution, ingredients
        FROM solutions
        WHERE disease = ? AND lang = ?
    """, (disease_name, lang))

    row = cur.fetchone()
    conn.close()

    # If a row is found
    if row:
        return {
            "organic_solution": row[0],
            "ingredients": row[1]
        }
    else:
        return {}
