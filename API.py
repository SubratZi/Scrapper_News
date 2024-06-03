from fastapi import FastAPI, Path
from typing import Optional

app =FastAPI()

inventory = {
    1:{
        "name":"milk",
        "price":360,
        "brand":"DairyDOOD"
        }
    }

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="ID of the item you would like to view",gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-item-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
