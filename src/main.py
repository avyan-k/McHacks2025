from task import *
from team import Team
from dev import Dev
from mlfq import *
import datetime
import database

def main():
    running = True
    default_team=Team()
    algorithm = MLFQ(default_team)
    while running:
        time_now = datetime.datetime.now().time()

        # Periodic all queue update every hour
        algorithm.periodic_queues_update(current_time=time_now)







if __name__ == '__main__':
    main()