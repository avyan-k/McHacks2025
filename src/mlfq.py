from collections import deque
import datetime
from task import *
from team import Team
import math
import database
import db_utils


class MLFQ:
    def __init__(self, team:Team=Team()):
        self.PRIORITY_QUEUES = {k:v for k,v in [(i, deque()) for i in range(1, 6)]}
        self.ONGOING_TASKS = []
        self.team = team
        self.database = database.open_database()

    def add_task_incoming(self, new_task:Task):
        queue_nb = self.update_task_priority(new_task)
        self.PRIORITY_QUEUES[queue_nb].appendleft(new_task)

        database.store_task_to_database(self.database, new_task)
            

    def nb_hours_until_deadline(self, deadline) :
        now = datetime.datetime.now()
        return ((deadline.year - now.year) * 8760 +
        (deadline.month - now.month) * 730 + (deadline.day - now.day) * 24)

    def get_delta_time_value(self, task:Task):
        """
        
        :param task: The task whose delta value we are calculating
        :return: task.deadline - current_time - task.estimated_time
        """
        return self.nb_hours_until_deadline(task.deadline) - math.ceil(task.estimated_time / 3600)

    def update_task_priority(self, task:Task):
        """
        Individually update a task's priority based on its delta time value.
        :param task:
        :return: task.priority
        """
        previous_priority = task.priority
        for i in range(1,5):
            interval = self.team.get_interval_by_queue(i)
            delta_time = self.get_delta_time_value(task)
            if delta_time > interval[0] and delta_time <= interval[1]:
                task.priority =  i

        print(f"Updated task {task.name} from {previous_priority} to {task.priority}")

        # Remove the task from the previous priority deque
        if task in self.PRIORITY_QUEUES[previous_priority]:
            self.PRIORITY_QUEUES[previous_priority].remove(task)

        # Add the task to its new priority queue
        self.PRIORITY_QUEUES[task.priority].appendleft(task)

        # Updating record in the database
        db_utils.update_record(self.database, name = "Tasks", set = "priority = ?", where = "id = ?", values=(task.priority, task.task_id))

        return task.priority

    def is_urgent_task(self, task:Task):
        """
        :param task:
        :return: Whether task is in priority 1 with negative delta time value, or not
        """
        interval = self.team.get_interval_by_queue(1)
        delta_time = self.get_delta_time_value(task)
        if delta_time < 0:
            return True
        else : return False


    def periodic_queues_update(self, current_time:datetime.time):
        # Since update_task_priority also moves it into another deque, we don't want
        # to unnecessarily check the same task twice, thus we keep track of the already checked ones.
        tasks_seen_before = dict()
        if current_time.minute == 0:
            for i in range(1,6):
                for task in  self.PRIORITY_QUEUES[i]:
                    if task.name not in tasks_seen_before.keys():
                        self.update_task_priority(task)
                        tasks_seen_before[task.name] = task
                    else :
                        # If the task was seen before in the update, don't check it twice.
                        pass

    def change_status_to_ongoing(self, task:Task):
        database.update_task(self.database, task, Status.ONGOING)

    def change_status_to_incomplete(self, task:Task):
        database.update_task(self.database, task, Status.INCOMPLETE)

    def change_status_to_complete(self, task:Task):
        database.update_task(self.database, task, Status.COMPLETE)


