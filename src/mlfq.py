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
        self.schedule()

    def add_to_ongoing(self, task):
        max_manpower_pts = team.max_manpower_pts
        total_manpower = 0 #how much manpower added so far
        for _,dev in team.devs.items()
            if (dev.current_task != None) : 
                continue
            if (dev.experience_level + total_manpower > manpower_pts):
            continue
        
            dev.current_task = task
            dev.task_start_time = datetime.datetime.now()
            task.attributed_devs.append(dev)
            team.manpower_pts -= dev.experience_level
            ONGOING_TASKS.append(task)
            change_status_to_ongoing(task)
            return True
        return False
    
    def add_to_full_ongoing(self, task):
        if (len(ONGOING_TASKS) == 0) :
            return false
        least_priority_task = ONGOING_TASKS[0]
        for task in ONGOING_TASKS.items():
            if (task.priority > least_priority_task):
                least_priority_task = task
        
        if (least_priority_task.priority <= task.priority): #ongoing has more priority
            return False 

        #replace tasks
        for (i in range(len(least_priority_task.attributed_devs))):
            least_priority_task.estimated_time -= nb_seconds_delta(task.task_start_time) * least_priority_task.attributed_devs[i].experience_level
            dev.current_task = None
            dev.task_start_time = None
            team.manpower_pts += dev.experience_level
        
        ONGOING_TASKS.remove(least_priority_task)
        if(least_priority_task.estimated_time > 0) : 
            add_task_incoming(least_priority_task) #add it back to queue
            change_status_to_incomplete(least_priority_task)
        else : 
            change_status_to_complete(least_priority_task)
        add_to_ongoing(task)
        task.change_status_to_ongoing(task)
        return True
        

    def schedule(self):
        manpower_pts = team.manpower_pts
        max_manpower_pts = team.max_manpower_pts
        for i in range(1,5):
            if (len(self.PRIORITY_QUEUES[i]) != 0):
                task = self.PRIORITY_QUEUES[i].popleft()
                if (manpower_pts > 0) : # set workers to task
                    if (add_to_ongoing(task) == False) :
                        self.PRIORITY_QUEUES[i].appendleft(task) 
                else :
                    if (add_to_full_ongoing(task) == False) :
                        self.PRIORITY_QUEUES[i].appendleft(task)
            

    def nb_hours_until_deadline(self, deadline) :
        now = datetime.datetime.now()
        return ((deadline.year - now.year) * 8760 +
        (deadline.month - now.month) * 730 + (deadline.day - now.day) * 24)

    def nb_seconds_delta(self, time) : #delta difference with respect to now
        now = datetime.datetime.now()
        return ((now.year - time.year) * 31536000 +
        (now.month - time.month) * 2628288 + (now.day - time.day) * 86400 +
        (now.minute - time.minute) * 60 - (now.minute - time.minute))

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

    # def periodic_ongoing_update(self) :
    #     for (task in ONGOING_TASKS) :
    #         for (i in range(len(task.attributed_devs))):
    #             least_priority_task.estimated_time -= nb_seconds_delta(task.task_start_time)* least_priority_task.attributed_devs[i].experience_level
            
    #         if (least_priority_task.estimated_time)
    
    def periodic_ongoing_update(self, current_time:datetime.time):

    def change_status_to_ongoing(self, task:Task):
        database.update_task(self.database, task, Status.ONGOING)

    def change_status_to_incomplete(self, task:Task):
        database.update_task(self.database, task, Status.INCOMPLETE)

    def change_status_to_complete(self, task:Task):
        database.update_task(self.database, task, Status.COMPLETE)


