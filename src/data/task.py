import sqlite3
from model.task import Task

DB_NAME = 'robinhood.db'
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

def init():
    curs.execute(
        """CREATE TABLE task(
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

def fow_to_model(row: tuple) -> Task:
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
