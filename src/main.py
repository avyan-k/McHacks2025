from task import *
from team import Team
from dev import Dev
from mlfq import *
import datetime
import database
import data_generation
from os.path import dirname, abspath, join
import sys
current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
sys.path.append(join(parent_dir, 'web_stuff'))
import app

def populate_database(algorithm:MLFQ, team:Team):
    task_list, dev_list = data_generation.generate_data()
    for task in task_list:
        algorithm.add_task_incoming(task)
    for dev in dev_list:
        team.add_dev(dev)

def main():
    running = True
    default_team=Team()
    default_team.priority_queues_intervals = {1:[0, 24], 2:[24, 168], 3:[168,672], 4:[672, 2016]}
    algorithm = MLFQ(default_team)

    populate_database(algorithm, default_team)
    default_team.update_manpower_global()
    app.app.run(debug=True)
    while running:
        time_now = datetime.datetime.now().time()
        while len(app.WEB_QUEUE) > 0:
            print(app.WEB_QUEUE)
            current_task = app.WEB_QUEUE.pop()
            algorithm.add_task_incoming(current_task)

        # Periodic all queue update every hour
        algorithm.periodic_queues_update(current_time=time_now)







if __name__ == '__main__':
    main()