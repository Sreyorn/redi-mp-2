import httpx

tasks = [
    {
        "title": "Study FastAPI",
        "description": "Review routes, request models and response schemas",
        "status": "done",
        "priority": "high",
        "tags": ["study", "backend"]
    },
    {
        "title": "Build sticky note UI",
        "description": "Style the task board with sticky note design",
        "status": "in_progress",
        "priority": "medium",
        "tags": ["frontend", "css"]
    },
    {
        "title": "Write API tests",
        "description": "Cover create, read, update and delete endpoints with pytest",
        "status": "todo",
        "priority": "high",
        "tags": ["testing", "backend"]
    },
    {
        "title": "Add filtering to GET /tasks",
        "description": "Support filtering by status, priority, tag and search keyword",
        "status": "todo",
        "priority": "high",
        "tags": ["backend", "feature"]
    },
    {
        "title": "Add Pydantic validation",
        "description": "Restrict status and priority to valid values using Literal types",
        "status": "todo",
        "priority": "medium",
        "tags": ["backend", "validation"]
    },
    {
        "title": "Create seed script",
        "description": "Write a script to populate the API with sample tasks on startup",
        "status": "done",
        "priority": "low",
        "tags": ["devtools"]
    },
    {
        "title": "Add task create form",
        "description": "Build an HTML form in the template so users can create tasks from the browser",
        "status": "todo",
        "priority": "medium",
        "tags": ["frontend", "feature"]
    },
    {
        "title": "Read Python docs",
        "description": "Go through the official Python docs on list comprehensions and generators",
        "status": "done",
        "priority": "low",
        "tags": ["study", "python"]
    },
    {
        "title": "Fix date format in template",
        "description": "Use strftime to show a clean date instead of raw datetime string",
        "status": "done",
        "priority": "low",
        "tags": ["frontend", "bugfix"]
    },
    {
        "title": "Push project to GitHub",
        "description": "Create a repo and push the full project with a clear README",
        "status": "todo",
        "priority": "high",
        "tags": ["devops", "submission"]
    }
]

for i, task in enumerate(tasks, start=1):
    response = httpx.post(f"http://localhost:8000/task/{i}", json=task)
    print(f"Task {i}: {response.status_code} - {task['title']}")
