from fastapi import FastAPI, HTTPException, status


tasks = [
    {"id":101, "title": "clean the room", "done": False},
    {"id":102, "title": "check mail inbox", "done": True},
    {"id":103, "title": "get grocery", "done": False}
]


app = FastAPI()

@app.get("/")
def root_info():
    
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def get_health():
    return { "status": "ok" }


@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_by_id(id: int):
    for task in tasks:
        if task["id"]==id:
            return task
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f"Task {id} not found"
    )

