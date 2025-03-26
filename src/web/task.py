from fastapi import APIRouter
from model.task import Task
import service.task as service

router = APIRouter(prefix = '/task')

@router.get('/')
def get_all() -> list[Task]:
    return service.get_all()

@router.get('/{task_id}')
def get_one(task_id: str) -> Task | None:
    return service.get_one(task_id)

@router.post('/')
def create(task: Task) -> Task:
    return service.create(task)

@router.patch('/')
def modify(task: Task) -> Task:
    return service.modify(task)

@router.put('/')
def replace(task: Task) -> Task:
    return service.replace(task)

@router.delete('/{task_id}')
def delete(task_id: str) -> bool:
    return service.delete(task_id)
