from model import Task

_tasks: list[Task] = [
    Task(
        summary='Задача 1',
        content='Содержимое задачи один.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        summary='Задача 2',
        content='Содержимое задачи два.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        summary='Задача трёх тел',
        content='Содержимое задачи трёх тел.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        summary='Задача на сообразительность',
        content='Содержимое задачи на сообразительность.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    ),
    Task(
        summary='Задача на производительность',
        content='Содержимое задачи на производительность.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    )
]

def get_tasks() -> list[Task]:
    return _tasks
