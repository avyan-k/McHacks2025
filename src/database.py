from db_utils import *
import sqlite3 as sql
from task import *
import datetime





def open_database():
    conn = connect_to_database("mchacks25.db")
    create_table(conn, "Tasks", """
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            deadline DATE,
            estimated_time INTEGER NOT NULL,
            priority INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """)

    create_table(conn, "Features", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn, "Bugs", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"Incoming_Task", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"Incomplete_Task", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"Ongoing_Tasks", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"Complete_Tasks", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)


    create_table(conn,"Devs", """
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            experience_level TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES Tasks
        """)
    
    create_table(conn,"Assigned_Tasks", """
            task_id INTEGER PRIMARY KEY,
            dev_id INTEGER NOT NULL,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
            FOREIGN KEY (dev_id) REFERENCES Devs(id)
            """)
    
    return conn
def store_task_to_database(database, task:Task):
    database_cursor = database.cursor()
    insert_record(database_cursor, "Tasks", "name, deadline, estimated_time, priority", (task.name, task.deadline, task.estimated_time,task.priority))
    pass
    
def get_all_incomplete_tasks():

    pass

if __name__ == "__main__":
    database = open_database()
    test_task = Task(name = "First",deadline = datetime.date.fromisoformat('20191204'), estimated_time = datetime.time.fromisoformat('04:23:01'),priority = 0)
    database.cursor().execute("SELECT name FROM PRAGMA_TABLE_INFO('Tasks')")
    print(database.cursor().fetchall())
    store_task_to_database(database,test_task)
    tasks = query_data(database.cursor(), "SELECT * FROM Tasks")
    print("Tasks:", tasks)
# searching through all incomplete task with a certain priority
# deleting from incoming table
# update 