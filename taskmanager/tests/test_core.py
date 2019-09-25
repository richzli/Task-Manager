from taskmanager.app import core
import os
import sqlite3
from contextlib import closing

### [id, name, type, description, priority, sticky, date] ###

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
    
    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            assert curs.execute("SELECT * FROM tasks WHERE id=1").fetchall()[0][2] == "todo"
            assert curs.execute("SELECT * FROM tasks WHERE name='talk to prof about lab'").fetchall()[0][4] == 2
            assert curs.execute("SELECT * FROM tasks").fetchall()[2][2] == "event"
            assert len(curs.execute("SELECT * FROM tasks WHERE type='event'").fetchall()) == 2

    print("test_add_task() success!")

def test_update_task():
    # assumes test_add_task() has already been run #

    core.update_task(1, {"description": "hw 1.5\nquestions 5, 12, 21, 24"})
    core.update_task(3, {"sticky": 1, "description": "remember to lift!"})
    core.update_task(2, {})
    
    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            assert curs.execute("SELECT * FROM tasks WHERE id=1").fetchall()[0][3] == "hw 1.5\nquestions 5, 12, 21, 24"
            assert curs.execute("SELECT * FROM tasks WHERE id=3").fetchall()[0][5] == 1
            assert curs.execute("SELECT * FROM tasks WHERE id=3").fetchall()[0][3] != None

    print("test_update_task() success!")

