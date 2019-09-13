import sqlite3
from os.path import exists
from contextlib import closing

def setup():
    if not exists("./taskmanager/data"):
        from os import makedirs
        makedirs("./taskmanager/data")
    
    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            command_task = """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT DEFAULT "todo",
            description TEXT,
            priority INTEGER DEFAULT 0,
            sticky INTEGER DEFAULT 0,
            date INTEGER
            );
            """
            command_done = """
            CREATE TABLE IF NOT EXISTS done (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT DEFAULT "todo",
            description TEXT,
            priority INTEGER DEFAULT 0,
            sticky INTEGER DEFAULT 0,
            date INTEGER
            );
            """
            #types: todo, event
            #persistent tasks: date = NULL
            
            curs.execute(command_task)
            curs.execute(command_done)
        conn.commit()

if __name__ == "__main__":
    setup()
