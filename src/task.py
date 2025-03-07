import datetime
from enum import Enum
class Status(Enum):
    INCOMING = 0
    ONGOING = 1
    COMPLETE = 2
    INCOMPLETE = 3
class Task:
    def __init__(self,name:str,deadline:datetime.date,estimated_time:int,priority:int,status:Status=Status.INCOMING):
        self.task_id = None
        self.attributed_devs = [] # ONCE MLFQ PUTS TASK IN "ONGOING" FOR THE FIRST TIME, ASSIGN DEVS
        self.name = name
        self.deadline = deadline
        self.estimated_time = estimated_time
        self.priority = priority
        self.status = status
    def __str__(self):
        return (f"Task of {self.name} with id: {self.task_id}, priority {self.priority}")
    @staticmethod
    def fromquery(query,status): # utility method for get all tasks SQL query method  to be turned into tasks
        task_id,name,deadline,estimated_time,priority,_ = query
        task = Task(name,deadline,estimated_time,priority,status)
        task.task_id = task_id
        return task





class Bug(Task):
    def __init__(self,deadline:datetime.date,estimated_time:datetime.time,priority:int):
        super.__init__(deadline,estimated_time,priority)

class Feature(Task):
    def __init__(self,deadline:datetime.date,estimated_time:datetime.time,priority:int):
        super.__init__(deadline,estimated_time,priority)

Task_NULL = Task(None, None, None, None,None)