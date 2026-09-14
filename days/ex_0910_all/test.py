import pydantic
from pydantic import BaseModel

class User(BaseModel):
    name : str # name 필드 생성
    age  : int # age 필드 생성

user = User(name="Kim", age="hello")