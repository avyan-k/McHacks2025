from collections import deque
import datetime
import Task

def mlfq():
    def __init__(self, dev_power, max_dev_power):
        self.PRIORITY_QUEUE1 = deque()
        self.PRIORITY_QUEUE2 = deque()
        self.PRIORITY_QUEUE3 = deque()
        self.PRIORITY_QUEUE4 = deque()
        self.PRIORITY_QUEUE5 = deque()
        self.dev_power = dev_power
        self.max_dev_power = max_dev_power

def add_task(new_task:Task):
    now = datetime.datetime.now()
    deadline = new_task.deadline
    deadline_hours = nb_hours_until_deadline(deadline)

def nb_hours_until_deadline(deadline) :
    now = datetime.datetime.now()
    return ((deadline.year - now.year) * 8760 + 
    (deadline.month - now.month) * 730 + (deadline.day - now.day) * 24)

