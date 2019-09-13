from taskmanager.app import core

def test_add_task():
    sample_task_1 = {"name": "finish math homework",
                     "type": "todo",
                     "description": "hw 1.4\nquestions 5, 12, 20, 23",
                     "sticky": 0,
                     "date": 1568521800} # 9/15/2019, 12:30 AM
    sample_task_2 = {"name": "talk to prof about lab",
                     "type": "event",
                     "priority": 2,
                     "sticky": 1,
                     "date": 1568741100} # 9/17/2019, 1:25 PM
    sample_task_3 = {"name": "daily workout",
                     "type": "event"}

    core.add_task(sample_task_1)
    core.add_task(sample_task_2)
    core.add_task(sample_task_3)
