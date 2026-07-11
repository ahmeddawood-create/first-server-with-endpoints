from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/home")
def home(name: str = "visitor"):
  return {"message":f"hello {name}"}

@myapp.get("/status")
def sitestatus():
  return {"status":"working"}
