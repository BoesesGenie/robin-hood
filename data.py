from model import Task

_tasks: list[Task] = [
    Task(
        summary='Задача 1',
        content='Содержимое задачи один.'
    ),
    Task(
        summary='Задача 2',
        content='Содержимое задачи два.'
    ),
    Task(
        summary='Задача трёх тел',
        content='Содержимое задачи трёх тел.'
    )
]

def get_tasks() -> list[Task]:
    return _tasks
