from db_utils import *
import sqlite3 as sql
from task import *




conn = connect_to_database("mchacks25.db")
crsr = conn.cursor()

create_table(crsr, "Tasks", """
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        deadline DATE NOT NULL,
        estimated_time INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """)

create_table(crsr, "Features", """

    """)

create_table(crsr, "Features", """
    """)

def store_task_to_database(task:Task):

    pass
def get_all_incomplete_tasks():

    pass
# searching through all incomplete task with a certain priority
# deleting from incoming table
# update 