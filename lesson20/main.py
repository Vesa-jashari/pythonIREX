from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World!!!"}

@app.get("/greet/")
def greet(name:str):
    return {"message":f"Hello {name}"}

@app.get("/items/")
def read_items():
    return {"item_id":["item1","item2","item3"]}
@app.post("/items/")
def create_item(name:str,price:float):
    return {"item":name,"item_price":price}
app.put("/items/{item_id}")
def update_item(item_id:int,name:str,price:float):
    return{"message":f"item is updated"}
@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return{"message":"The item is deleted "}