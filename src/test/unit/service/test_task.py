from model.task import Task
from service import task as code

sample = Task(
    id='1',
    summary='Задача 1',
    content='Содержимое задачи один.',
    done=False,
    start=0,
    period=0,
    created_at=0,
    updated_at=0
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one('1')
    assert resp == sample


def test_get_missing():
    resp = code.get_one('42')
    assert resp is None
