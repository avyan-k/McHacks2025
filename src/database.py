from db_utils import *
import sqlite3 as sql
from task import *





def open_database():
    conn = connect_to_database("mchacks25.db")
    crsr = conn.cursor()
    create_table(crsr, "Tasks", """
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        deadline DATE,
        estimated_time INTEGER NOT NULL,
        priority INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """)

    create_table(crsr, "Features", """
            FOREIGN KEY (id) REFERENCES Tasks
        """)

    create_table(crsr, "Bugs", """
            FOREIGN KEY (id) REFERENCES Tasks
        """)

    create_table(crsr,"""Incoming Task,
            FOREIGN KEY (id) REFERENCES Tasks
        """)

    create_table(crsr,""" Incomplete Task,
            FOREIGN KEY (id) REFERENCES Tasks
        """)

    create_table(crsr,"""Ongoing Tasks,
            FOREIGN KEY (id) REFERENCES Tasks
        """)

    create_table(crsr,"""Complete Tasks,
            FOREIGN KEY (id) REFERENCES Tasks
        """)
    
    create_table(crsr,"""Devs
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            experience_level TEXT NOT NULL
        """)
    
    create_table(crsr,"""AssignedTask
            FOREIGN KEY (id) REFERENCES Tasks

            """)
    create_table(crsr,"""Devs
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            experience_level TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES Tasks
        """)
    return conn,crsr
def store_task_to_database(database_cursor, task:Task):
    insert_record(database_cursor, "Tasks", "name, deadline, estimated_time", (task.name, task.deadline, 30))
    pass
    
def get_all_incomplete_tasks():

    pass


# searching through all incomplete task with a certain priority
# deleting from incoming table
# update 