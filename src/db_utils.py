import sqlite3 as sql

def connect_to_database(db_name):
    return sql.connect(db_name)

def create_table(connection, name, schema):    
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({schema})")
    connection.commit()

def insert_record(connection, name, columns, values):
    cursor = connection.cursor()
    placeholders = ", ".join("?" for _ in values)  # Generate "?" placeholders
    query = f"INSERT INTO {name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)
    connection.commit()

def query_data(cursor, query: str, params = None) :
    cursor.execute(query, params or ())
    return cursor.fetchall()

def update_record(connection, name: str, set, where, values):
    cursor = connection.cursor()
    query = f"UPDATE {name} SET {set} WHERE {where}"
    cursor.execute(query, values)
    connection.commit()

def delete_record(conn: sql.Connection, name, where, values):
    cursor = conn.cursor()
    query = f"DELETE FROM {name} WHERE {where}"
    cursor.execute(query, values)
    conn.commit()


if __name__ == "__main__":
    connection = connect_to_database("example.db")
    cursor = connection.cursor()



    connection.close()