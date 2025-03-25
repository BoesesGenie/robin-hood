from fastapi import FastAPI
from web import task

app = FastAPI()

app.include_router(task.router)

@app.get('/')
def top():
    return 'top here'

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=False)