# FASTAPI SERVER FOR TASK APP

## How to use it?

- Download these files on your PC
- Create and activate a virtual environment (optional)
    - In your terminal, run:
        - python -m venv venv
        - venv/Scripts/activate
- Install FastAPI and other libraries (must)
    -In your terminal, run:
        - pip install fastapi[standard]
- Run the server using the command in your terminal:
    - fastapi dev
- Now, you can run the curl commands to use the app, or you can open http://127.0.0.1:8000/ in your browser
- Example curl command: curl "http://127.0.0.1:8000/tasks/101"
- You can also access the Swagger UI made interactive documentation, on http://127.0.0.1:8000/docs



## What is ths app about?

This is a task managing CRUD app to manage your daily tasks efficiently. It consists of  endpoints.

## Table for Endpoints

| Endpoint | Description | Parameters | Response |
| :--- | :--- | :--- | :--- |
| `GET /` | Welcome the user | *None* | `{"name": str, "version": str, "endpoints": list}` |
| `GET /health` | Check if server is working | *None* | `{"status": "ok"}` |
| `GET /tasks` | Display all the tasks stored in the app | *None* | `List[Task]` |
| `GET /tasks/{id}` | Display the task based on ID | **Path:** `id` *(int)* | `Task` or `404 Not Found` |
| `POST /tasks` | Add a new task to the app | **Body:** `{"title": str}` | `Task` *(201 Created)* or `400 Bad Request` |
| `PUT /tasks/{id}` | Update the existing tasking based on ID | **Path:** `id` *(int)*<br>**Body:** `{"title"?: str, "done"?: bool}` | `Task` or `400 Bad Request` / `404 Not Found` |
| `DELETE /tasks/{id}` | Remove a task from app based on ID | **Path:** `id` *(int)* | *204 No Content* or `404 Not Found` |

## screenshot of Endpoints in Swagger UI Documentation

![alt text](image.png)
