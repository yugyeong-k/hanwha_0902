import streamlit as st
import requests #웹을 통해 데이터를 주고받을 수 있게 해주는 라이브러리

API_URL = "http://127.0.0.1:8003"

st.header("사용자 목록")
response = requests.get(f"{API_URL}/users")
if response.status_code == 200:
    users = response.json()
    for user in users:
        st.write(
            f"ID: {user['id']} / 이름: {user['name']}"
        )
else:
    st.error("사용자 조회 실패")

st.header("사용자 추가")
user_id = st.number_input(
    "ID",
    min_value=1, #입력 최솟값 설정
    step=1
)

user_name = st.text_input("이름")

if st.button("사용자 추가"):
    data = {
        "id": user_id,
        "name": user_name
    }

    response = requests.post(
        f"{API_URL}/users",
        json=data
    )

    if response.status_code == 200:
        st.success("사용자 추가 완료")
        st.rerun()
    else:
        st.error(response.text)

st.header("사용자 삭제")
delete_id = st.number_input(
    "삭제할 ID",
    min_value=1, #입력 최솟값 설정
    step=1
)

if st.button("사용자 삭제"):
    data = {
        "id": user_id
    }

    response = requests.delete(
        f"{API_URL}/users/{delete_id}",
        json=data
    )

    if response.status_code == 200:
        st.success("사용자 삭제 완료")
        st.rerun()
    else:
        st.error(response.text)

st.header("사용자 수정")

update_id = st.number_input(
    "수정 할 ID",
    min_value=1, #입력 최솟값 설정
    step=1
)  

user_name = st.text_input("수정 할 이름")

if st.button("사용자 수정"):
    data = {
        "name": user_name
    }

    response = requests.put(
        f"{API_URL}/users/{user_id}",
        json = data
    )

    if response.status_code == 200:
        st.success("사용자 수정 완료")
        st.rerun()
    else:
        st.error(response.text)