import sqlite3 as sql

def connect_to_database(db_name):
    return sql.connect(db_name)

def create_table(cursor, name, schema):    
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({schema})")
    connection.commit()

def insert_record(cursor, name, columns, values):
    placeholders = ", ".join("?" for _ in values)  # Generate "?" placeholders
    query = f"INSERT INTO {name} ({columns}) VALUES ({placeholders})"
    print(query)
    cursor.execute(query, values)
    connection.commit()

def query_data(cursor, query: str, params) :
    cursor.execute(query, params or ())
    return cursor.fetchall()

def update_record(connection, name: str, set, where, values):
    cursor = connection.cursor()
    query = f"UPDATE {name} SET {set} WHERE {where}"
    cursor.execute(query, values)
    connection.commit()



if __name__ == "__main__":
    connection = connect_to_database("example.db")
    cursor = connection.cursor()

    create_table(cursor, "users", """
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """)
    users = query_data(cursor, "SELECT * FROM users")
    print("Users:", users)

    insert_record(cursor, "users", "name, email, age", ("Alice", "alice@example.com", 30))
    insert_record(cursor, "users", "name, email, age", ("Bob", "bob@example.com", 25))
    insert_record(cursor, "users", "name, email, age", ("Charlie", "charlie@example.com", 35))
    users = query_data(cursor, "SELECT * FROM users")
    print("Users:", users)
    update_record(connection, "users", "age = ?", "name = ?", (31, "Alice"))



    connection.close()