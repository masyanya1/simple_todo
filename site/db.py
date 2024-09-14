import sqlite3
from typing import Union, List
from tools import get_date, datetime

con = sqlite3.connect('database.db', check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            compl_date DATETIME,
            compl INTEGER
            )''')

def get_tasks(date: datetime = None) -> Union[List[sqlite3.Row], None]:
    all_tasks = cur.execute('''SELECT * FROM tasks''').fetchall()
    return all_tasks

def get_task(id: int = 0) -> Union[sqlite3.Row, None]:
    task = cur.execute('''SELECT * FROM tasks WHERE id = ?''', (id,)).fetchone()
    return task

def create_task(**kwargs) -> None:
    try:
        title = kwargs['title']
        description = kwargs.get('description')
        compl_date = kwargs.get('compl_date')
        
        cur.execute('''INSERT INTO tasks (title, description, compl_date)
        VALUES (?, ?, ?)''', (title, description, compl_date,))
        con.commit()

        return True

    except KeyError:
        return False

    except Exception as err:
        print(err)

def update_task() -> None:
    pass

def delete_task(id: int) -> None:
    cur.execute('''DELETE FROM tasks WHERE id = ?''', (id,))
    con.commit()
