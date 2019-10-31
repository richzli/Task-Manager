from ..app import core
from ..setup import setup
import os
import sqlite3
import unittest
import shutil
from contextlib import closing

### [id, name, type, description, priority, sticky, date] ###

def reset():
    if os.path.exists("./taskmanager/data"):
        shutil.rmtree("./taskmanager/data")

def add_task():
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
                     "type": "event",
                     "repeating": 127}

    core.add_task(sample_task_1)
    core.add_task(sample_task_2)
    core.add_task(sample_task_3)

def update_task():
    # assumes add_task() has already been run #

    core.update_task(1, {"description": "hw 1.5\nquestions 5, 12, 21, 24"})
    core.update_task(3, {"sticky": 1, "description": "remember to lift!"})
    core.update_task(2, {})

def finish_task():
    # assumes add_task() has already been run #

    core.finish_task(2)

class TestCore(unittest.TestCase):

    def setUp(self):
        setup.setup()
    
    def tearDown(self):
        reset()

    def test_add(self):
        add_task()
        with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
            with closing(conn.cursor()) as curs:
                self.assertEqual(curs.execute("SELECT * FROM tasks WHERE id=1").fetchall()[0][2], "todo")
                self.assertEqual(curs.execute("SELECT * FROM tasks WHERE name='talk to prof about lab'").fetchall()[0][4], 2)
                self.assertEqual(curs.execute("SELECT * FROM tasks").fetchall()[2][2], "event")
                self.assertEqual(len(curs.execute("SELECT * FROM tasks WHERE type='event'").fetchall()), 2)

        print("test_add() success!")

    def test_update(self):
        add_task()
        update_task()

        with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
            with closing(conn.cursor()) as curs:
                self.assertEqual(curs.execute("SELECT * FROM tasks WHERE id=1").fetchall()[0][3], "hw 1.5\nquestions 5, 12, 21, 24")
                self.assertEqual(curs.execute("SELECT * FROM tasks WHERE id=3").fetchall()[0][5], 1)
                self.assertNotEqual(curs.execute("SELECT * FROM tasks WHERE id=3").fetchall()[0][3], None)   

        print("test_update() success!")    

    def test_finish(self):
        add_task()
        finish_task()

        print("test_finish() success!")