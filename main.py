from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional


tasks = [
    {"id":101, "title": "clean the room", "done": False},
    {"id":102, "title": "check mail inbox", "done": True},
    {"id":103, "title": "get grocery", "done": False}
]

class PostBody(BaseModel):
    title: str

class UpdateBody(BaseModel):
    title: Optional[str]
    done: Optional[bool]


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
  

@app.put("/tasks/{id}")
def update_task(id: int, body: UpdateBody):
    
    if not body.model_dump(exclude_unset=True):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is no content in body")

    for task in tasks:
        if task["id"]==id:
            task.update(body.model_dump(exclude_unset=True))
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task of id {id} not found"

    )  




@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    for task in tasks:
        if task["id"]==id:
            tasks.remove(task)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task of id {id} not found"
    )

