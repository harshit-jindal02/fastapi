# FastAPI ToDo List

This is a FastAPI-based ToDo List backend, converted from the original Flask implementation. It provides a RESTful API for managing tasks, using SQLite as the database and SQLAlchemy as the ORM.

## Features

- Add, edit, toggle, and delete tasks
- Mark all tasks as finished
- CORS enabled for frontend integration
- Docker support

## Requirements

- Python 3.8+
- pip

## Setup (Local)

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the app:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at [http://localhost:8000](http://localhost:8000).

## Setup (Docker)

1. **Build the Docker image:**
    ```bash
    docker build -t fastapi-todo .
    ```

2. **Run the container:**
    ```bash
    docker run -p 8000:8000 fastapi-todo
    ```

## API Endpoints

| Method | Endpoint           | Description                |
|--------|--------------------|----------------------------|
| GET    | /api/todos         | List all tasks             |
| POST   | /task              | Add a new task             |
| POST   | /toggle            | Toggle a task's done state |
| POST   | /edit              | Edit a task's content      |
| DELETE | /delete/{task_id}  | Delete a task              |
| POST   | /finished          | Mark all tasks as done     |

### Example Task Object

```json
{
  "id": 1,
  "content": "Sample task",
  "done": false
}
```

## Notes

- The SQLite database file (`todo.db`) will be created automatically in the working directory.
- Adjust CORS settings in `main.py` as needed for your frontend.
# fastapi
