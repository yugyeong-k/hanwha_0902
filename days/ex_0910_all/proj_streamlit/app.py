import streamlit as st
import re
import requests # 웹을 통해 데이터를 주고받을 수 있게 해주는 라이브러리

# 런타임에 절대 변하면 안되는 값이라 대문자로 설정(상수)
FASTAPI_URL = "http://127.0.0.1:8000"

# 메뉴
st.sidebar.title("메뉴")

if "login_user" in st.session_state:
    menu_list = ["ChatBot","로그아웃"]
else:
    menu_list = ["로그인","회원가입"]

menu = st.sidebar.selectbox(
    "메뉴를 선택하세요.",
    menu_list
)

# 회원가입
if menu == "회원가입":
    # 사용자 가입 화면
    st.subheader("📄 회원가입")      # 조금 작음
    with st.form("create_user_form"):
        user_id = st.text_input("ID를 입력하세요.")
        user_password = st.text_input("8자리 이상의 비밀번호를 입력하세요", type="password")
        user_name = st.text_input("이름을 입력하세요.")
        user_age = st.number_input("나이를 입력하세요.", min_value=15, step=1)
        user_date = st.date_input("가입일을 선택하세요.")
        
        if st.form_submit_button("가입"):
            # st.write("① 버튼 눌림")
            data = {
                "id"       : user_id,
                "name"     : user_name,
                "password" : user_password,
                "age"      : user_age,
                "date"     : user_date.isoformat()
            }
            
            # st.write("② 데이터 생성:", data)
            
            response = requests.post(
                f"{FASTAPI_URL}/users",
                json = data
            )    
            
            # st.write("③ 요청 완료")
            # st.write("상태 코드:", response.status_code)
            # st.write("응답:", response.text)
    
            if response.status_code == 200:
                st.success("가입 완료되었습니다.") 
            else:
                st.error(response.json()["detail"])
                
elif menu == "로그인":
    # 로그인 화면
    st.subheader("🔒 로그인")
    with st.form("login_form"):
        login_id = st.text_input("ID를 입력하세요.")
        login_password = st.text_input("비밀번호를 입력하세요.", type="password")
        
        if st.form_submit_button("로그인"):
            data = {
                "id" : login_id,
                "password" : login_password
            }
            
            response = requests.post(
                f"{FASTAPI_URL}/login",
                json = data
            )
            
            if response.status_code == 200:
                
                st.session_state.login_user = login_id
                st.success("로그인되었습니다.")
                st.rerun()
            else:
                st.error(response.json()["detail"])
                
elif menu == "ChatBot":
    st.subheader("🗨️ ChatBot")

    # 대화 저장공간
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 처음 들어왔을 때 로봇이 먼저 인사
    if len(st.session_state.messages) == 0:
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"{st.session_state.login_user}님, 무엇을 도와드릴까요?"
        })

    # 저장된 대화 출력
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # 사용자 입력
    prompt = st.chat_input("메시지를 입력하세요.")

    if prompt:

        # 사용자 메시지 저장
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        # 사용자 메시지 출력
        with st.chat_message("user"):
            st.write(prompt)

        # 로봇 응답
        response = "대답 할 수 없음"

        # 로봇 응답 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        # 로봇 응답 출력
        with st.chat_message("assistant"):
            st.write(response)


elif menu == "로그아웃":
    st.session_state.pop("login_user", None)
    st.success("로그아웃되었습니다.")
    st.rerun()