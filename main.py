from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


tasks = [
    {"id":101, "title": "clean the room", "done": False},
    {"id":102, "title": "check mail inbox", "done": True},
    {"id":103, "title": "get grocery", "done": False}
]

class PostBody(BaseModel):
    title: str
    


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

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def add_task(body: PostBody):
  ids = [task["id"] for task in tasks]
  newid = max(ids)+1
  if body.title is None or body.title=="" or body.title=="string":
     raise HTTPException(
         status_code=status.HTTP_400_BAD_REQUEST,
         detail="No title provided or just 'string'"
     )

  else:
      newbody: dict ={
         "id": newid, "title" : body.title, "done": False
      }
      tasks.append(newbody)
      return newbody
