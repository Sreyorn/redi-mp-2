from fastapi import FastAPI

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
async def addTask(task_id):
    newTask = {
        "id": 12,
        "title": "task1",
        "description":"testing task 1 adding",
        "status":"todo",
        "priority":"high",
        "tags":["work", "personal"],
        "created_at":"02-12-1999"
    }
    tasks[task_id] = newTask
    return newTask