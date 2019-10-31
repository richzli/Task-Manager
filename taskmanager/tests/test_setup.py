from ..setup import setup
from os.path import exists
import unittest

class TestSetup(unittest.TestCase):
    def test_setup(self):
        setup.setup()

        self.assertTrue(exists("./taskmanager/data"))
        self.assertTrue(exists("./taskmanager/data/tasks.db"))

        print("test_setup() success!")