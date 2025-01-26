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

    create_table(conn,"ONGOING_Task", """
            task_id INTEGER PRIMARY KEY,
            FOREIGN KEY (task_id) REFERENCES Tasks(id)
        """)

    create_table(conn,"COMPLETE_Task", """
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
            task_id INTEGER,
            dev_id INTEGER,
            FOREIGN KEY (task_id) REFERENCES Tasks(id),
            FOREIGN KEY (dev_id) REFERENCES Devs(id),
            PRIMARY KEY (task_id, dev_id)
            """)
    
    return conn
def store_task_to_database(database, task:Task):
    cursor = database.cursor()
    insert_record(database, "Tasks", "name, deadline, estimated_time, priority", (task.name, task.deadline, task.estimated_time,task.priority))
    cursor.execute("SELECT last_insert_rowid()")
    task_id = cursor.fetchone()[0]
    if task_id:
        insert_record(database, "INCOMING_Task", "task_id", (task_id,))
    task.task_id = task_id
    task.status = Status.INCOMING
    return task_id

def update_task(database,task:Task, status:Status):
    assert task.status != Status.COMPLETE
    old_status_name_string = task.status.name
    new_status_name_string = status.name
    delete_record(database, f"{old_status_name_string}_Task", "task_id = ?", (task.task_id,))
    insert_record(database, f"{new_status_name_string}_Task", "task_id", (task.task_id,))
    task.status = status
    
def get_all_tasks_of_status(status:Status):
    status_name_string = status.name
    return [Task.fromquery(query,status) for query in query_data(database.cursor(), f"SELECT Tasks.* FROM Tasks JOIN {status_name_string}_Task ON Tasks.id = {status_name_string}_Task.task_id;")]

def get_all_tasks_of_status_with_priority(status:Status,priority:int):
    status_name_string = status.name
    return [Task.fromquery(query,status) for query in query_data(database.cursor(), f"SELECT Tasks.* FROM Tasks JOIN {status_name_string}_Task ON Tasks.id = {status_name_string}_Task.task_id WHERE Tasks.priority = {priority};")]

if __name__ == "__main__":
    database = open_database()
    test_task1 = Task(name = "First",deadline = datetime.date.fromisoformat('20191204'), estimated_time = 10,priority = 0, status=Status.INCOMING)
    test_task2 = Task(name = "First",deadline = datetime.date.fromisoformat('20161204'), estimated_time = 5,priority = 3, status=Status.INCOMING)
    store_task_to_database(database,test_task1)
    store_task_to_database(database,test_task2)
    tasks = query_data(database.cursor(), "SELECT * FROM Tasks")
    print("Tasks:", tasks)
    print(get_all_tasks_of_status(Status.INCOMING))
    update_task(database,test_task1,status=Status.COMPLETE)
    print(query_data(database.cursor(), "SELECT Tasks.* FROM Tasks JOIN COMPLETE_Task ON Tasks.id = COMPLETE_Task.task_id;"))
    print(*get_all_tasks_of_status_with_priority(Status.INCOMING,3))
    print("hi")

