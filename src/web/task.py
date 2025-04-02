from fastapi import APIRouter, HTTPException
from model.task import Task
import service.task as service
from error import Duplicate, Missing

router = APIRouter(prefix = '/task')

@router.get('/')
def get_all() -> list[Task]:
    return service.get_all()

@router.get('/{task_id}')
def get_one(task_id: str) -> Task:
    try:
        return service.get_one(task_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.post('/')
def create(task: Task) -> Task:
    try:
        return service.create(task)
    except Duplicate as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.patch('/')
def modify(task: Task) -> Task:
    try:
        return service.modify(task)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.put('/')
def replace(task: Task) -> Task:
    try:
        return service.replace(task)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.delete('/{task_id}')
def delete(task_id: str) -> bool:
    try:
        return service.delete(task_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
