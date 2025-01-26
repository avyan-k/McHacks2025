import datetime
from enum import Enum
class Status(Enum):
    INCOMING = 0
    ONGOING = 1
    COMPLETE = 2
    INCOMPLETE = 3
class Task:
    def __init__(self,name:str,deadline:datetime.date,estimated_time:int,priority:int,status:Status):
        self.name = name
        self.deadline = deadline
        self.estimated_time = estimated_time
        self.priority = priority
        self.status = status

    def fromquery(self,query): 
        task_id,deadline,estimated_time,priority = query
        pass

class Bug(Task):
    def __init__(self,deadline:datetime.date,estimated_time:datetime.time,priority:int):
        super.__init__(deadline,estimated_time,priority)
    def __init__(self, query):
        super().__init__(query)

class Feature(Task):
    def __init__(self,deadline:datetime.date,estimated_time:datetime.time,priority:int):
        super.__init__(deadline,estimated_time,priority)
    def __init__(self, query):
        super().__init__(query)

Task_NULL = Task(None, None, None, None)