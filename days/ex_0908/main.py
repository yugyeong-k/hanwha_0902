from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    key_alexnet = "alexnet"
    key_resnet = "resnet"
    key_lenet = "lenet"

fask_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

# http://127.0.0.1:8000/users/admin
@app.get("/users/admin")
async def read_user_admin():
    return {"사용자 ID": "admin"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"사용자 ID": user_id}

#http://127.0.0.1:8000/users
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

@app.get("/models/{model_name}")
async def gat_mode(model_name: ModelName):

    # alexnet 키를 요청하면, 값을 return, http://127.0.0.1:8000/models/alexnet
    if model_name is ModelName.key_alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    # resnet 값을 요청하면, 키를 return, http://127.0.0.1:8000/models/resnet
    if model_name.value == "resnet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    # 그 외 요청 값, http://127.0.0.1:8000/models/lenet
    return {"model_name": model_name, "message": "Have some residuals"}

# http://127.0.0.1:8000/items/
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # return fask_items_db [0 : 10]
    return fask_items_db[skip : skip + limit]

# http://127.0.0.1:8000/items/test
# http://127.0.0.1:8000/items/test?q=int(1)
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {item_id: item_id}
    if q: 
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item