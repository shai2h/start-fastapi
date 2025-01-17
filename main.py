from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
    ]

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)

