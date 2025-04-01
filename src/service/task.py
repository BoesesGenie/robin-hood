from model.task import Task
import data.task as data

def get_all() -> list[Task]:
    return data.get_all()

def get_one(task_id: str) -> Task | None:
    return data.get_one(task_id)

def create(task: Task) -> Task:
    return data.create(task)

def replace(task: Task) -> Task:
    return data.replace(task)

def modify(task: Task) -> Task:
    return data.modify(task)

def delete(task_id: str) -> bool:
    return data.delete(task_id)
