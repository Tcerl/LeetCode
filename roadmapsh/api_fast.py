from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    if q is None:
        return {"item_id": item_id}
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

@app.get("/search/")
async def search_items(q: str | None = None):
    if q is None:
        return {"message": "No query provided", "q": q}
    return {"query": q}