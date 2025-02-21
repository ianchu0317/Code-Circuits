from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None


shopping_cart = []


# Crear una tarea
@app.post("/add_item/")
def add_item(item: Item):
    if item not in shopping_cart:
        shopping_cart.append(item)
        msg = f"Item '{item.name}' added"
    else:
        msg = f"Item '{item.name}' already in list"
    return msg

# Ver carro de compra
@app.get("/view_items/")
def view_items():
    return shopping_cart


@app.delete("/delete/{id}")
def delete_item(id: int):
    for item in shopping_cart:
        if item.id == id:
            shopping_cart.remove(item)
    return f"Item id={id} successfully remove from shopping cart"
