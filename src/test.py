from task import Task
from task import Status
from dev import Dev
from team import Team
import mlfq
import datetime


def run_test():
    task1 = Task(name="Bug 1", deadline=datetime.datetime(2025, 1, 27),
                 estimated_time=5, priority=5, status=Status.INCOMING)
    dev1 = Dev(1, "Jean-Michel", 4)
    team1 = Team(devs={1: dev1}, manpower_pts=0, max_mp_percentage=0.5,
                priority_queues_intervals={1: [0,24], 2:[24, 48], 3:[48,100], 4:[100, 200]})
    team1.update_manpower_global()

    # Test instance of MLFQ
    test = mlfq.MLFQ(team1)
    print(test.PRIORITY_QUEUES)
    print(type(test.PRIORITY_QUEUES[0]))
    test.add_task(task1)

run_test()

