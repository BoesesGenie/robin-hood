from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Task list"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", reload=True)
