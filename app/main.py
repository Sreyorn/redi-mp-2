from fastapi import FastAPI

print('FastAPI and uvicorn are working')
app = FastAPI()

@app.get("/")
async def test():
    testObj={
        "message": "This is a test object"
    }
    return testObj