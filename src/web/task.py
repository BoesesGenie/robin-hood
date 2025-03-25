from fastapi import APIRouter
from src.model.task import Task
import src.fake.task as service

router = APIRouter(prefix = '/task')

@router.get('/')
def get_all() -> list[Task]:
    return service.get_all()

@router.get('/{id}')
def get_one(id: str) -> Task | None:
    return service.get_one(id)

@router.post('/')
def create(task: Task) -> Task:
    return service.create(task)

@router.patch('/')
def modify(task: Task) -> Task:
    return service.modify(task)

@router.put('/')
def replace(task: Task) -> Task:
    return service.replace(task)

@router.delete('/{id}')
def delete(task_id: str) -> bool:
    return service.delete(task_id)
