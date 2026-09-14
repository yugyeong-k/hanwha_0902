from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 임시 메모리 DB 생성
items_db = {}

# 아이템 번호 카운트
id_counter = 1

# 요청 데이터 형식
class ItemCreate(BaseModel):
    name: str
    price: int

# 응답 데이터 형식
class Item(BaseModel):
    id: int
    name: str
    price: int

# 1. Create
@app.post("/api/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global id_counter

    new_item = {
        "id": id_counter,
        "name": item.name,
        "price": item.price
    }

    items_db[id_counter] = new_item
    id_counter += 1

    return new_item

# 2. Read All
@app.get("/api/items", response_model=list[Item])
def get_items():
    return list(items_db.values())

# 3. Read Detail
@app.get("/api/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="아이템이 없습니다."
        )

    return items_db[item_id]

# 4. Update
@app.put("/api/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="아이템이 없습니다."
        )

    items_db[item_id]["name"] = item.name
    items_db[item_id]["price"] = item.price

    return items_db[item_id]

# 5. Delete
@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail="아이템이 없습니다."
        )

    deleted_item = items_db.pop(item_id)

    return {
        "message": "삭제 완료",
        "deleted": deleted_item
    }

