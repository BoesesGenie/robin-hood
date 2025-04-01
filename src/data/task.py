import sqlite3
from model.task import Task

DB_NAME = 'robinhood.db'
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

curs.execute(
    """CREATE TABLE IF NOT EXISTS task(
        id TEXT PRIMARY KEY,
        summary TEXT,
        content TEXT,
        done NUMERIC,
        start NUMERIC,
        period NUMERIC,
        created_at NUMERIC,
        updated_at NUMERIC
    )"""
)

def row_to_model(row: tuple) -> Task:
    id, summary, content, done, start, period, created_at, updated_at = row

    return Task(
        id=id,
        summary=summary,
        content=content,
        done=done,
        start=start,
        period=period,
        created_at=created_at,
        updated_at=updated_at
    )

def model_to_dict(task: Task) ->dict:
    return task.model_dump()

def get_one(task_id: str) -> Task:
    query = 'SELECT * FROM task WHERE id=:id'
    params = {'id': task_id}
    curs.execute(query, params)
    row = curs.fetchone()

    return row_to_model(row)

def get_all() -> list[Task]:
    query = 'SELECT * FROM task'
    curs.execute(query)
    rows = list(curs.fetchall())

    return [row_to_model(row) for row in rows]

def create(task: Task):
    query = """INSERT INTO task VALUES
        (:id, :summary, :content, :done, :start, :period, :created_at, :updated_at)"""
    params = model_to_dict(task)
    curs.execute(query, params)

def modify(task: Task):
    return task

def replace(task: Task):
    return task

def delete(task_id: str):
    query = "DELETE FROM task WHERE id = :id"
    params = {'id': task_id}
    curs.execute(query, params)