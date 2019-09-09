import sqlite3
from os.path import exists
from contextlib import closing

def setup():
    if not exists("../data"):
        from os import makedirs
        makedirs("../data")
    
    with closing(sqlite3.connect("../data/tasks.db")) as conn:
        curs = conn.cursor()
        
        command_task = """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT DEFAULT "task",
        description TEXT,
        priority INTEGER DEFAULT 0,
        sticky INTEGER DEFAULT 0,
        due_date INTEGER
        );
        """
        command_done = """
        CREATE TABLE IF NOT EXISTS done (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT DEFAULT "task",
        description TEXT,
        priority INTEGER DEFAULT 0,
        sticky INTEGER DEFAULT 0,
        due_date INTEGER
        );
        """
        #persistent tasks: due date = NULL
        
        curs.execute(command_task)
        curs.execute(command_done)
        
        conn.commit()

if __name__ == "__main__":
    setup()
