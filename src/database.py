import os
from db_utils import *
import sqlite3 as sql
from task import *
import datetime





def open_database(filename = "mchacks25.db"):
    if os.path.isfile(filename):
        os.remove(filename)
    conn = connect_to_database(filename)
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

    create_table(conn,"INCOMING_Task", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"INCOMPLETE_Task", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"ONGOING_Tasks", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"COMPLETE_Tasks", """
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
    cursor = database.cursor()
    insert_record(database, "Tasks", "name, deadline, estimated_time, priority", (task.name, task.deadline, task.estimated_time,task.priority))
    cursor.execute("SELECT last_insert_rowid()")
    task_id = cursor.fetchone()
    if task_id:
        insert_record(database, "INCOMING_Task", "task_id", (task_id))
    task.task_id = task_id
    return task_id

def update_task(task:Task, status:Status):
    assert task.status != Status.COMPLETE
    old_status_name_string = task.status.name
    new_status_name_string = status.name
    delete_record()


    pass

    
def get_all_incoming_tasks():
    return query_data(database.cursor(), "SELECT Tasks.* FROM Tasks JOIN INCOMING_Task ON Tasks.id = INCOMING_Task.task_id;")

if __name__ == "__main__":
    database = open_database()
    test_task = Task(name = "First",deadline = datetime.date.fromisoformat('20191204'), estimated_time = 10,priority = 0, status=Status.COMPLETE)
    store_task_to_database(database,test_task)
    tasks = query_data(database.cursor(), "SELECT * FROM Tasks")
    print("Tasks:", tasks)
    print(get_all_incoming_tasks())
    update_task(test_task,status=Status.INCOMING)
    print(status.name)
# searching through all incomplete task with a certain priority
# deleting from incoming table
# update 