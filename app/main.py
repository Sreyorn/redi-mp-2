from fastapi import FastAPI, HTTPException
from app.models import Task 

app = FastAPI()

# tasks objects
tasks = {}

@app.get("/test")
async def test():
    testObj={
        "message": "This is a test object"
    }
    return testObj

@app.get("/")
async def getAllTasks():
    return tasks

# {
#   "id": int,
#   "title": string,
#   "description": string,
#   "status": "todo" | "in_progress" | "done",
#   "priority": "low" | "medium" | "high",
#   "tags": [string],
#   "created_at": datetime
# }
@app.post("/task/{task_id}")
async def addTask(task_id:int, task: Task):
    # Pydantic models are immutable by default, so we can't do task.id = task_id directly
    # model_copy() creates a new task objet with the id field updated
    task = task.model_copy(update={"id":task_id})
    tasks[task_id] = task.model_dump()
    return task

# get a single task by id
@app.get("/task/{task_id}")
async def getTaskById(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task does not exist")
    task = tasks[task_id]
    return task

# update a task 
@app.put("/task/{task_id}")
async def updateTask(task_id:int, newTask:Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task doesn't exist")
    updated_task = newTask.model_copy(update={"id":task_id})
    tasks[task_id] = updated_task.model_dump()
    return updated_task

@app.delete("/task/{task_id}")
async def deleteTask(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task does not exist, can't be deleted")
    tasks.pop(task_id)
    return tasks