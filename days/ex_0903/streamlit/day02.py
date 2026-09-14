import streamlit as st
import textwrap

def show():

    st.title("Day 02", icon="📖")
    st.caption("2026년 09월 03일")
    st.divider()

    # 1. 가상환경
    st.markdown("### 1. Python 가상환경")
    st.markdown("""
    - Python :blue-badge[가상환경] 생성
    - 프로젝트별로 :blue-badge[독립적인 Python 실행 환경] 구성
    """)
    st.code(
        textwrap.dedent(r"""
        # 가상환경 생성
        python -m venv .venv

        # 가상환경 활성화
        .venv\Scripts\activate

        # 가상환경 비활성화
        deactivate
        """),
        language="bash"
    )

    st.divider()

    # 2. Streamlit
    st.markdown("### 2. Streamlit")
    st.caption("Streamlit 설치 및 실행")
    st.code(
        textwrap.dedent("""
        # Streamlit 설치
        pip install streamlit

        # 실행할 Python 파일 실행
        streamlit run app.py
        """),
        language="bash"
    )
    st.divider()     

    # 3. Python 기본 문법 공부
    st.markdown("### 3. Python 기본 문법 공부")
    st.caption("W3Schools로 Python 기본 문법 학습")

    # 자료 구조
    st.markdown(":violet-badge[자료구조] 종류")
    with st.expander("자료구조 종류 보기"):
        st.caption("여러 개의 데이터를 하나의 변수에 저장하는 방법")
        st.markdown("""
        * 리스트: `list` 
        * 튜플: `tuple`
        * 세트: `set`
        * 딕셔너리: `dict`
        """)
    with st.expander("실습 예제"):
        st.code(
            textwrap.dedent("""
            # 리스트: 여러 값을 순서대로 저장하고 수정할 수 있음
            fruits = ["사과", "바나나", "포도"]

            # 튜플: 여러 값을 순서대로 저장하고 수정할 수 없음
            colors = ("빨강", "파랑", "초록")

            # 세트: 중복된 값을 저장하지 않음
            numbers = {1, 2, 2, 3}

            # 딕셔너리: 키와 값의 쌍으로 데이터를 저장
            user = {"name": "홍길동", "age": 30}

            # 각 자료구조 출력
            print(fruits)
            print(colors)
            print(numbers)
            print(user)
            """),
            language="python"
        )

        st.caption("결과")
        st.code(
            textwrap.dedent("""
            ['사과', '바나나', '포도']
            ('빨강', '파랑', '초록')
            {1, 2, 3}
            {'name': '홍길동', 'age': 30}
            """),
            language="text"
        )

    # 인덱싱 · 슬라이싱
    st.markdown(":violet-badge[인덱싱 · 슬라이싱] 사용 방법")
    with st.expander("실습 예제"):
        st.caption("**인덱싱**은 인덱스를 이용해 특정 값을 가져오고, **슬라이싱**은 범위를 지정해 여러 값을 가져옴")
        st.code(
            textwrap.dedent("""
            fruits = ["사과", "바나나", "포도", "딸기", "수박"]

            # 인덱스는 0부터 시작, 0: 첫 번째 값, 1: 두 번째 값
            print(fruits[0])
            print(fruits[1])

            # 음수 인덱스는 뒤에서부터 접근, -1: 마지막 값, -2: 뒤에서 두 번째 값
            print(fruits[-1])
            print(fruits[-2])

            # 슬라이싱: [시작:끝], 끝 인덱스는 포함하지 않음
            print(fruits[1:3])

            # 처음부터 3번 인덱스 전까지
            print(fruits[:3])            

            # 2번 인덱스부터 마지막까지
            print(fruits[2:])    
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            사과
            바나나
            수박
            딸기
            ['바나나', '포도']
            ['사과', '바나나', '포도']
            ['포도', '딸기', '수박']
            """),
            language="text"
        )

    # 리스트
    st.markdown(":violet-badge[리스트] 사용 방법")
    with st.expander("실습 예제"):
        st.caption("**리스트**는 여러 개의 값을 저장하며, 값을 **추가, 수정, 삭제**할 수 있음")
        st.code(
                textwrap.dedent("""
                fruits = ["사과", "바나나", "포도"]     # 리스트 생성

                fruits.append("딸기")
                ruits.insert(1, "수박")
                fruits[0] = "복숭아" # 인덱스를 이용해 값 수정
                fruits.remove("포도")
                fruits.pop()
                fruits.sort()
                fruits.reverse()
                print(len(fruits))

                print(fruits)
                """),
                language="python"
            )

        st.caption("주요 메서드")
        st.markdown("""
            - `append()` : 마지막에 값 추가
            - `insert()` : 원하는 위치에 값 추가
            - `remove()` : 특정 값 삭제
            - `pop()` : 특정 위치의 값 삭제 (인덱스를 생략하면 마지막 값 삭제)
            - `sort()` : 값 정렬(문자열은 가나다순, 숫자는 작은 수부터 정렬)
            - `reverse()` : 리스트 순서 뒤집기
            - `len()` : 리스트의 길이 확인
            """)

        st.caption("결과")
        st.code(
                textwrap.dedent("""
                3
                ['수박', '복숭아', '바나나']
                """),
                language="text"
            )

    # 딕셔너리
    st.markdown(":violet-badge[딕셔너리] 사용 방법")
    with st.expander("실습 예제"):
        st.caption("**딕셔너리**는 **키와 값의 쌍**으로 데이터를 저장")

        st.code(
            textwrap.dedent("""
            # 딕셔너리 생성
            user = {
                "name": "홍길동",
                "age": 30,
                "city": "서울"
            }

            # 키를 이용해 값 가져오기
            print(user["name"])

            # 값 수정
            user["age"] = 31

            # 새로운 키와 값 추가
            user["job"] = "개발자"

            # 키와 값 삭제
            del user["city"]

            # 딕셔너리 출력
            print(user)
            """),
            language="python"
        )
        st.caption("결과")
        st.code(
            textwrap.dedent("""
            홍길동
            {'name': '홍길동', 'age': 31, 'job': '개발자'}
            """),
            language="text"
        )

    # 함수
    st.markdown(":violet-badge[함수] 정의 방법")
    with st.expander("실습 예제"):
        st.caption(
            "**def**는 함수를 **정의**할 때 사용하며, **return**은 함수의 **결과**를 **반환**"
        )
        st.code(
            textwrap.dedent("""
            # def 함수 정의
            def hello(name):
                # 전달받은 name을 넣어 결과 반환
                return "안녕하세요, " + name

            # hello 함수 호출
            result = hello("홍길동")

            # 결과 출력
            print(result)
            """),
            language="python"
        )
        st.caption("결과")
        st.code(
            "안녕하세요, 홍길동",
            language="text"
        )

        # 종합 실습

    # 예외처리
    st.markdown(":violet-badge[예외처리] 사용 방법")
    with st.expander("실습 예제"):
        st.caption("예외가 발생할 수 있는 코드를 안전하게 처리")
        st.markdown("""
        - `try`    : 예외가 발생할 수 있는 코드 실행
        - `except` : 예외 발생 시 처리
        - `finally`: 예외 발생 여부와 관계없이 마지막에 항상 실행
        """)

        st.code(
            textwrap.dedent("""
            try:
                number = int("안녕하세요")
                print(number)

            except ValueError:
                print("숫자로 변환할 수 없습니다.")

            finally:
                print("실행 완료")
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            숫자로 변환할 수 없습니다.
            실행 완료
            """),
            language="text"
        )

    st.markdown(":violet-badge[종합 실습]")
    with st.expander("실습 예제"):

        st.code(
            textwrap.dedent("""
            def create_user(name, age):
                return {
                    "name": name,
                    "age": age
                }

            users = [
                create_user("홍길동", 30),
                create_user("김철수", 25),
                create_user("이영희", 28)
            ]

            for user in users:
                print(user)
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            {'name': '홍길동', 'age': 30}
            {'name': '김철수', 'age': 25}
            {'name': '이영희', 'age': 28}
            """),
            language="text"
        )

    