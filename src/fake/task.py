from model.task import Task

_tasks: list[Task] = [
    Task(
        id='1',
        summary='Задача номер 1',
        content='Содержимое задачи один.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        id='2',
        summary='Задача 2',
        content='Содержимое задачи два.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        id='3',
        summary='Задача трёх тел',
        content='Содержимое задачи трёх тел.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        id='4',
        summary='Задача на сообразительность',
        content='Содержимое задачи на сообразительность.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        id='5',
        summary='Задача на производительность',
        content='Содержимое задачи на производительность очень интересное.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    )
]


def get_all() -> list[Task]:
    return _tasks


def get_one(task_id: str) -> Task | None:
    for _task in _tasks:
        if _task.id == task_id:
            return _task

    return None

def create(task: Task) -> Task:
    return task

def modify(task: Task) -> Task:
    return task

def replace(task: Task) -> Task:
    return task

def delete(task_id: str) -> bool:
    return True
