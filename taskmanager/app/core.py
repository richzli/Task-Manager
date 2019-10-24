import sqlite3
from contextlib import closing

def add_task(data: dict) -> None:
    """
    Adds a task to the tasks table.

    @param data A dictionary holding pairs of column names and values.
    """
    
    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            fields = str(tuple(data.keys())).replace("'", "")
            values = tuple(data.values())
            insert = "(" + ("?,"*len(values))[:-1] + ")"

            sql = "INSERT INTO tasks " + fields + " VALUES " + insert

            curs.execute(sql, values)
        conn.commit()

def update_task(taskid: int, data: dict) -> None:
    """
    Updates a task in the tasks table.

    @param taskid The ID of the task to be updated.
    @param data A dictionary holding pairs of column names and values.
    """

    if data == {}:
        return
    
    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            fields = tuple(data.keys())
            values = tuple(data.values())
            update = " = ?, ".join(fields) + " = ?"
            
            sql = "UPDATE tasks SET " + update + " WHERE id = ?"

            curs.execute(sql, values + (taskid,))
        conn.commit()

def finish_task(taskid: int) -> None:
    """
    Moves a task from the tasks table to the done table.

    @param taskid The ID of the task to be moved.

    """

    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            sql1 = "INSERT INTO done SELECT * FROM tasks WHERE id=?"
            sql2 = "DELETE FROM tasks WHERE id=?"

            curs.execute(sql1, (taskid,))
            curs.execute(sql2, (taskid,))
        conn.commit()
            
def unfinish_task(taskid: int) -> None:
    """
    Moves a task from the done table to the tasks table.

    @param taskid The ID of the task to be moved.

    """

    with closing(sqlite3.connect("./taskmanager/data/tasks.db")) as conn:
        with closing(conn.cursor()) as curs:
            sql1 = "INSERT INTO tasks SELECT * FROM done WHERE id=?"
            sql2 = "DELETE FROM done WHERE id=?"

            curs.execute(sql1, (taskid,))
            curs.execute(sql2, (taskid,))
        conn.commit()

def get_next_date(repeating: int, currdate: int) -> int:
    return 0

def get_prev_date(repeating: int, currdate: int) -> int:
    return 0
