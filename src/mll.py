from collections import deque
import datetime
from task import Task
from team import Team
import math 


class mll:
    def __init__(self, team:Team=Team()):
        self.PRIORITY_QUEUES = {k:v for k,v in [(i, deque()) for i in range(1, 6)]}
        self.ONGOING_TASKS = []
        self.team = team


    def schedule(self):
        manpower_pts = team.manpower_pts
        max_manpower_pts = team.max_manpower_pts
        for i in range(1,5):
            while (manpower_pts > 0) : # set workers to task
                    if (max_manpower_pts <= manpower_pts):
                        # add to ongoing ls (max_manpower)
                    else :
                        #add to ls (manpower)
            else :
                #replace task (task, i)
            

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
        self.PRIORITY_QUEUES[previous_priority].remove(task)

        # Add the task to its new priority queue
        self.PRIORITY_QUEUES[task.priority].appendleft(task)

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

    def 


