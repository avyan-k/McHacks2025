from task import *
from team import Team
from dev import Dev
from mlfq import *
import datetime
import database
import data_generation


def populate_database(algorithm:MLFQ, team:Team):
    task_list, dev_list = data_generation.generate_data()
    for task in task_list:
        algorithm.add_task_incoming(task)
    for dev in dev_list:
        team.add_dev(dev)

def main():
    running = True
    default_team=Team()
    algorithm = MLFQ(default_team)

    populate_database(algorithm, default_team)
    default_team.update_manpower_global()

    while running:
        time_now = datetime.datetime.now().time()

        # Periodic all queue update every hour
        algorithm.periodic_queues_update(current_time=time_now)







if __name__ == '__main__':
    main()