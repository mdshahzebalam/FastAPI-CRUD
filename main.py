from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item | None = None):
    
    return item

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})  
    return results