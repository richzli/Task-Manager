import sqlite3

def setup():
    conn_task = sqlite3.connect("task.db")
    conn_done = sqlite3.connect("done.db")

    curs_task = conn_task.cursor()
    curs_done = conn_done.cursor()
    
    command = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT DEFAULT "task",
    description TEXT,
    priority INTEGER DEFAULT 0,
    due_date INTEGER
    );
    """
    #persistent tasks: due date = NULL

    curs_task.execute(command)
    curs_done.execute(command)

    conn_task.commit()
    conn_done.commit()

    conn_task.close()
    conn_done.close()

if __name__ == "__main__":
    setup()
