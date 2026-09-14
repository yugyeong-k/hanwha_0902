from datetime import date
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id       : str
    password : str
    name     : str
    age      : int
    date     : date

class LoginUser(BaseModel):
    id       : str
    password : str

users = [
        User(
        id="test123",
        password="12345678",
        name="테스트",
        age=20,
        date=date.today()
    )
]

app = FastAPI()

# POST - 사용자 가입
@app.post("/users")
def create_user(user : User):
    # existing_user : 기존 가입자
    for existing_user in users:
        if existing_user.id == user.id:
            raise HTTPException(
                status_code = 400,
                detail = "이미 존재하는 ID 입니다."
            )
    if len(user.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="비밀번호는 8자리 이상이어야 합니다."
        )
    if user.date > date.today():
        raise HTTPException(
            status_code = 400,
            detail="가입일은 오늘 이후로 설정할 수 없습니다."
        )
    
    users.append(user)
    return(user)

# POST - 로그인
@app.post("/login")
def login_user(login_user : LoginUser):
    # existing_user : 기존 가입자
    for existing_user in users:
        if existing_user.id == login_user.id:
            if existing_user.password == login_user.password:
                return
            
            raise HTTPException(
                status_code=400,
                detail="비밀번호가 일치하지 않습니다."
            )
        
    raise HTTPException(
        status_code=400,
        detail="존재하지 않는 ID입니다."
    )
