import sqlite3
from os.path import exists
from contextlib import closing

def setup():
    dbfile = "./taskmanager/data"
    if not exists(dbfile):
        from os import makedirs
        makedirs(dbfile)
    
    with closing(sqlite3.connect(dbfile + "/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            command_task = """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT DEFAULT "todo",
            description TEXT,
            priority INTEGER DEFAULT 0,
            sticky INTEGER DEFAULT 0,
            date INTEGER,
            repeating INTEGER DEFAULT 0
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
            date INTEGER,
            repeating INTEGER DEFAULT 0
            );
            """
            command_deleted = """
            CREATE TABLE IF NOT EXISTS deleted (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT DEFAULT "todo",
            description TEXT,
            priority INTEGER DEFAULT 0,
            sticky INTEGER DEFAULT 0,
            date INTEGER,
            repeating INTEGER DEFAULT 0
            );
            """
            #types: todo, hw, event
            #persistent tasks: date = NULL
                #repeating tasks: repeating = some integer
                #0 = sunday, 1 = monday, ..., 6 = saturday
                #stored in binary, so 1 = sunday 2 = monday... 64 = saturday
                #so if repated 
            
            
            curs.execute(command_task)
            curs.execute(command_done)
            curs.execute(command_deleted)
        conn.commit()

if __name__ == "__main__":
    setup()
