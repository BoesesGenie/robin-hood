from fastapi import FastAPI
from data import get_tasks

app = FastAPI()

@app.get("/")
def daily():
    return get_tasks()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", reload=True)
