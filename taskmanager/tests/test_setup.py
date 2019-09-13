from taskmanager.setup import setup
from os.path import exists

def test_setup():
    setup.setup()

    assert exists("./taskmanager/data")
    assert exists("./taskmanager/data/tasks.db")

    print("test_setup() success!")
