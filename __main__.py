"""
import os
import shutil

def run_tests():
    import unittest
    #import taskmanager.tests.test_setup
    import taskmanager.tests.test_core

if __name__ == "__main__":
   run_tests()
"""
import unittest

import taskmanager.tests.test_core
import taskmanager.tests.test_setup