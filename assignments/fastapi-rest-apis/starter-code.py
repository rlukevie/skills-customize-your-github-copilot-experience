from typing import List

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class ItemIn(BaseModel):
    name: str = Field(min_length=1)
    completed: bool = False


class Item(ItemIn):
    id: int


items: List[Item] = []
next_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemIn):
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items.append(item)
    next_id += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemIn):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated = Item(id=item_id, **payload.model_dump())
            items[index] = updated
            return updated

    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail="Item not found")
