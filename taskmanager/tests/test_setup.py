from ..setup import setup
from os.path import exists

def test_setup():
    setup.setup(1)

    assert exists("./taskmanager/data")
    assert exists("./taskmanager/data/tasks.db")

    print("test_setup() success!")
