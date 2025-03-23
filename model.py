from pydantic import BaseModel

class Task(BaseModel):
    summary: str
    content: str
