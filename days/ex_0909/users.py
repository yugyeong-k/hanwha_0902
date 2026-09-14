from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str

class UserNameUpdate(BaseModel):
    name : str

app = FastAPI()

# 임시 데이터 생성
users = [
    {"id": 1, "name": "KIM"},
    {"id": 2, "name": "LEE"},
]

# GET - 전체 사용자 조회
@app.get("/users")
def get_users():
    return users #users에 저장된 임시 데이터 전체 반환

# # GET - 특정 사용자 조회
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     for user in users: # users에 있는 데이터를 하나씩 꺼내어 user에 할당
#         if user["id"] == user_id: # 전달받은 user_id와 현재 user의 id가 같은지 비교
#             return user # id가 일치하는 user 데이터 반환

#     return {"message": "User not found"}

# POST - 사용자 추가
@app.post("/users")
def create_user(user: User): # 요청 받은 데이터를 User 클래스 형식으로 받아서 user에 저장
    for test in users:
        if test["id"] == user.id:
            raise HTTPException(
                status_code=400,
                detail="이미 존재하는 ID입니다."
            )
        
    users.append(user.model_dump()) # user를 users 리스트에 추가
    return user # 추가한 user 데이터 반환

# DELETE - 사용자 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id : int): 
    for user in users:
        if user["id"] == user_id:
            users.remove(user) # users 리스에서 user 삭제
            return {"message": "User deleted"}
        
    return {"message": "User not found"} 

# PUT - 사용자 정보 수정
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UserNameUpdate):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.name # 이름 수정
            return {"message": "User updated", "user": user}
                    
    return {"message": "User not found"}