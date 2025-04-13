from model.task import Task
from .init import curs, conn, IntegrityError
from error import Missing, Duplicate

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

    if row:
        return row_to_model(row)

    raise Missing(msg=f"Task {task_id} not found")

def get_all() -> list[Task]:
    query = 'SELECT * FROM task'
    curs.execute(query)
    rows = list(curs.fetchall())

    return [row_to_model(row) for row in rows]

def create(task: Task) -> Task:
    # query = """INSERT INTO task VALUES
    #    (:id, :summary, :content, :done, :start, :period, :created_at, :updated_at)"""
    # params = model_to_dict(task)
    #
    # try:
    #     curs.execute(query, params)
    #     conn.commit()
    # except IntegrityError:
    #     raise Duplicate(msg=f"Task {task.id} already exists")

    return get_one(task.id)

def modify(task: Task):
    # query = """UPDATE task
    #     SET summary = :summary,
    #     content = :content,
    #     done = :done,
    #     start = :start,
    #     period = :period,
    #     created_at = :created_at,
    #     updated_at = :updated_at
    #     WHERE id = :id"""
    # params = model_to_dict(task)
    #
    # curs.execute(query, params)
    #
    # if curs.rowcount == 1:
    #     return get_one(task.id)
    # else:
    #     raise Missing(msg=f"Task #{task.id} not found.")

    return task # TODO: remove!

def replace(task: Task):
    return task

def delete(task_id: str):
    # query = "DELETE FROM task WHERE id = :id"
    # params = {'id': task_id}
    # curs.execute(query, params)
    #
    # if curs.rowcount != 1:
    #     raise Missing(msg=f"Task {task_id} not found")

    return # TODO: remove!
