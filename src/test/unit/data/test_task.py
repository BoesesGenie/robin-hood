import os
import pytest
from model.task import Task
from error import Missing, Duplicate
# important! set this BEFORE data module import (see data.init)
os.environ['TASK_SQLITE_DB'] = ':memory:'
from data import task

@pytest.fixture
def sample() -> Task:
    return Task(
        id='1',
        summary='Задача 1',
        content='Содержимое задачи один.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    )

def test_create(sample):
    resp = task.create(sample)

    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = task.create(sample)

def test_get_one(sample):
    resp = task.get_one(sample.id)

    assert resp == sample

def test_modify(sample):
    sample.done = True
    resp = task.modify(sample)

    assert resp == sample

def test_modify_missing():
    missing: Task = Task(
        id='2',
        summary='Задача 2',
        content='Содержимое задачи два.',
        done=False,
        start=0,
        period=0,
        created_at=0,
        updated_at=0
    )

    with pytest.raises(Missing):
        _ = task.modify(missing)

def test_delete(sample):
    resp = task.delete(sample.id)

    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = task.delete(sample.id)
