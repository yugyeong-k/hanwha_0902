from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
    username: str
    email: EmailStr # 이메일 형식 자동 검증(pydantic)
    password: str

class Item(BaseModel):
    name: str
    price: int
    desc: str | None = None

items_db = {
    101: "노트북",
    102: "스마트폰",
    103: "무선 이어폰"
}

# 임시 사용자 데이터
users_db = {
    1: "홍길동",
    2: "김철수",
    3: "이영희"
}

app = FastAPI()

# DELETE-------------------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(
            status_code = 404,
            detail = "사용자를 찾을 수 없습니다."
        )

    deleted_user_name = users_db.pop(user_id)
    
    return {
        "message": "사용자가 성공적으로 삭제되었습니다.",
        "deleted_id": user_id,
        "deleted_name": deleted_user_name,
        "remaining_users": users_db  # 남은 사용자 목록 확인용
    }

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="해당 아이템이 존재하지 않습니다.")
    
    deleted_item_name = items_db.pop(item_id)
    
    return {
        "message": "아이템이 성공적으로 삭제되었습니다.",
        "deleted_id": item_id,
        "deleted_name": deleted_item_name,
        "current_items": items_db  # 남은 아이템 목록
    }

# POST-------------------------------------
@app.post("/users/signup")
async def create_user(user: UserSignUp):
    #비밀번호 길이 검증
    if len(user.password) < 8:
        raise HTTPException(
            status_code = 400, #에러 코드 설정
            detail = "비밀번호는 최소 8자리 이상이어야 합니다." #에러 메세지 설정
        )

    return{
        "message": f"{user.username}님의 회원가입이 완료되었습니다.",
        "user_email": user.email
    }

@app.post("/items/")
async def items(item: Item):
    return{
        "msg"   : "물건 등록 완료",
        "name"  : item.name,
        "price" : item.price,
        "desc"  : item.desc
    }

# GET-------------------------------------
# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello"}

# Query Parameter
# http://127.0.0.1:8000/user/name?name=john
@app.get("/user/name")
async def name(name: str):
    return {"message": f"my name is {name}"}

# Path Parameter
# http://127.0.0.1:8000/user/15
@app.get("/user/{age}")
async def user(age: int):
    return {"message": f"age: {age}"}

