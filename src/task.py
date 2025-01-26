import datetime
class Task:
    def __init__(self,name:str,deadline:datetime.date,estimated_time:datetime.time,priority:int):
        self.name = name
        self.deadline = deadline
        self.estimated_time = estimated_time
        self.priority = priority

    def __init__(self,query): 
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