import fastapi
from fastapi import FastAPI
app = FastAPI()
#END POINTS:-
#GET
#POST
#PUT
#DELETE
# for Setting end point
@app.get("/")
def home(): #root
  return{"Data":"Test"}
  #if u cahange here the data on API changes in real time
@app.get("/about")
def about():
  return{"Data":"Help"}
  
#setting Inventory
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  age : float
  brand : Optional[str] = None

inventory = {}


# ": int is called type hinting to hint the API that it should be int datatype"
#Here also we can ask for that booze Ex_ def get_item(item_id : int, item_name : string)
#PATH
from fastapi import Path
@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(None,description =  "Whaterver item_id is and its constrains")):
  return inventory[item_id]

from fastapi import Query

@app.get("/get-by-name")
def get_item(name: str = Query(None, title = "Name", description = "Name of item")):
  for item_id in inventory:
    if inventory[item_id].name == name:
      return inventory[item_id]
  return {"Data":"Not Found"}

# to post (add things)
@app.post("/create-item/{item_id}")
def create_item(item_id : int , item: Item):
  if item_id in inventory:
   return{"Error" : "Item already exists" }

  inventory[item_id] = item
  return inventory[item_id]

#to update
class UpdateItem(BaseModel):
  name : Optional[str] = None
  age : Optional[float] = None
  brand : Optional[str] = None

@app.put("/update-item/{item_id")
def update_item(item_id : int,item : UpdateItem):
    if item_id not in inventory:
     return{"Error" : "Item does not exists" }
    if item.name != None:
      inventory[item_id].name = item.name

    if item.age != None:
      inventory[item_id].age = item.age

    if item.brand != None:
      inventory[item_id].brand = item.brand
    return inventory[item_id]

  # to Delete
@app.delete("/delete-item")
def delete_item(item_id : int = Query(...,description = "Item to dlete")):
  if item_id not in inventory:
   return{"Error" : "Item does not exists" }

  del inventory[item_id]
  return {"Sucess":"Item gone!"}