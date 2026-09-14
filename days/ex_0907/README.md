# Pydantic

### 1. 기본 데이터 검증과 타입 변환

```python
    from pydantic import BaseModel, PositiveInt

    class User(BaseModel):
    id : int
    name : str = "John Doe"
    signup_ts : datetime | None
    tastes : dict[str, PositiveInt] =

    external_data = {
    'id' : 123,
    'signup_ts' : '2019-06-01 12:22',
    'tastes' : {
        'wine' : 9,
        b'cheese' : 7,  #b: bytes데이터
        'cabbage' : '1',
        },
    }

    user = User(**external_data)

    print(user.id)
    print(user.signup_ts)
    print(user.tastes)
    print(user.model_dump())
```

### 세번째 제목

----

* 목록1
* 목록2
* 목록3

---

