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
    ),
    Task(
        summary='Задача на сообразительность',
        content='Содержимое задачи на сообразительность.'
    ),
    Task(
        summary='Задача на производительность',
        content='Содержимое задачи на производительность.'
    )
]

def get_tasks() -> list[Task]:
    return _tasks
