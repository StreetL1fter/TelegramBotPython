import sqlite3 as sql
from pathlib import Path

def create_users_table():
    current_file = Path(__file__)
    db_path = current_file.parent/ 'databasebytraining.db'
    with sql.connect(db_path) as conn: 
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL)""",)


def save_user(user_id, name, email):
    current_file = Path(__file__)
    db_path = current_file.parent/ 'databasebytraining.db'
    with sql.connect(db_path) as conn:  
        cur = conn.cursor()
        array = [    
                "INSERT INTO users(id,name,email)VALUES(?,?,?)"
        ]
        for x in array:
            cur.execute(x,(user_id,name,email))
        conn.commit()



def payments_save_user():
    current_file = Path(__file__)
    db_path = current_file.parent/ 'databasebytraining.db'
    with sql.connect(db_path) as conn:  
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.execute("CREATE TABLE IF NOT EXISTS orders(" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "user_id INTEGER NOT NULL," \
        "product_name TEXT NOT NULL," \
        "amount INTEGER NOT NULL,"
        "status TEXT NOT NULL,"
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
        "payment_id TEXT UNIQUE," \
        "FOREIGN KEY(user_id) REFERENCES users(id) )")
        conn.commit()


def payments_orders():
    current_file = Path(__file__)
    db_path = current_file.parent/ 'databasebytraining.db'
    with sql.connect(db_path) as conn:  
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.execute("SELECT DISTINCT name from users")
        names = cur.fetchall()
        return names
