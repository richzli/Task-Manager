import os
import shutil

def run_tests():
    import taskmanager.tests.test_setup as setup
    import taskmanager.tests.test_core as core

    setup.test_setup()
    core.test_add_task()
    core.test_update_task()

if __name__ == "__main__":
    import taskmanager.tests.test_core as core
    core.reset()
    
    
