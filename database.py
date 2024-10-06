import sqlite3

#Creating the Database
#Now, let's create a database using SQLite to store the user's names:
def create_database():
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS names (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )""")
    conn.commit()
    conn.close()


def insert(name):
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("INSERT INTO names (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_names():
    conn = sqlite3.connect("names.db")
    
    c = conn.cursor()
    c.execute("SELECT * FROM names")
    
    rows = c.fetchall()
    conn.close()
    return rows
