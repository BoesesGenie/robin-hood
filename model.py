from pydantic import BaseModel

class Task(BaseModel):
    summary: str
    content: str
    done: bool
    start: int
    period: int
    created_at: int
    updated_at: int
