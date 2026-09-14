import streamlit as st
import textwrap

def show():
    st.title("Day 01", icon="📖")
    st.caption("2026년 09월 02일")

    st.divider()

    #1. Python 설치
    st.markdown("### 1. Python 설치")
    st.markdown("""
    - Python 3.12.10 설치
    - 설치 시 :blue-badge[Add Python to PATH] 체크
    - 설치 후 환경변수 설정 확인
    - 설치 후 cmd에서 :blue-badge[python --version] 명령어로 설치 확인
    """)
    st.link_button(
        label="Python 3.12.10 다운로드",
        url="https://www.python.org/downloads/release/python-31210/"
    )

    st.divider()

    #2. Visual Studio Code 설치
    st.markdown("### 2. Visual Studio Code 설치")
    st.markdown("""
    - Visual Studio Code 설치
    - Python 관련 확장 프로그램 설치 
        - :green-badge[Python], :green-badge[Pylance], :green-badge[Python Debugger], :green-badge[Python Environments]
    - 한국어 확장 프로그램 설치
        - :green-badge[Korean Language Pack for Visual Studio Code]
    """)
    st.link_button(
        label="Visual Studio Code 다운로드",
        url="https://code.visualstudio.com/download"
    )

    st.divider()

    #3. Python 기본 문법 공부
    st.markdown("### 3. Python 기본 문법 공부")
    st.caption("W3Schools로 Python 기본 문법 학습")

    # 주석
    st.markdown(":violet-badge[주석] 작성 방법")
    with st.expander("실습 예제"):
        st.code(
            "# 주석은 #으로 작성",
            language="python"
        )
        st.caption("단축키 : :gray-badge[**Ctrl + /**]")
        
    #변수
    st.markdown(":violet-badge[변수] 사용 방법")
    with st.expander("실습 예제"):
        st.code(
            textwrap.dedent("""
            name = "홍길동"
            age = 30
            height = 175.5

            # name 변수에 저장된 값을 출력
            print(name)

            # 변수끼리 연산도 가능
            print(age + 1)
            """),
            language="python"
        )
        st.caption("**변수**는 **데이터를 저장하는 공간**, 변수명은 **밑줄(_)**, **영문자**, **숫자**로 구성 가능, **숫자로 시작 불가**")

    # 출력
    st.markdown(":violet-badge[출력] 방법")
    with st.expander("실습 예제"):
        st.code(
            textwrap.dedent("""
            name = "홍길동"
            age = 30

            # 변수에 저장된 값을 출력
            print(name)
            print(age)

            # 여러 개의 값을 sep 매개변수로 구분하여 출력
            print(name, age, sep=',')
            """),
            language="python"
        )

        st.caption("결과")
        st.code(
            "홍길동\n30\n홍길동,30",
            language="python"
        )

    # 데이터 유형
    st.markdown(":violet-badge[데이터 유형] 정리")
    with st.expander("데이터 유형 보기"):
        st.caption("데이터 종류에 따라 변수에 저장되는 데이터 유형이 달라짐")
        st.markdown("""
        * 문자열: `str`
        * 숫자형: `int` · `float` · `complex`
        * 시퀀스: `list` · `tuple` · `range`
        * 매핑: `dict`
        * 집합: `set` · `frozenset`
        * 불리언: `bool`
        * 이진: `bytes` · `bytearray` · `memoryview`
        * None 타입: `NoneType`
        """)
    with st.expander("실습 예제"):
        st.code(
                textwrap.dedent("""
                service_name: str = "summary-api"   #문자열 변수
                max_length: int = 100               #정수형 변수
                temperature: float = 0.2            #실수형 변수
                is_enabled: bool = True             #불리언 변수

                # type() : 변수 데이터 유형을 확인하는 함수
                print(type(service_name), type(max_length))
                """),
                language="python"
            )
        st.caption("결과")
        st.code("<class 'str'> <class 'int'>", language="python")

    # 연산자
    st.markdown(":violet-badge[연산자] 정리")

    # 산술 연산자
    with st.expander("산술 연산자"):
        st.caption("숫자를 계산할 때 사용하는 연산자")
        st.dataframe({
            "연산자": ["+", "-", "*", "/", "%", "**", "//"],
            "의미": ["덧셈", "뺄셈", "곱셈", "나눗셈", "나머지", "거듭제곱", "몫"],
        })
        st.caption("실습 예제")
        st.code(textwrap.dedent("""
        a = 10
        b = 5

        print(a + b)  
        print(a - b)  
        print(a * b)  
        print(a / b)  
        print(a % b)  
        print(a ** b) 
        print(a // b) 
        """),
        language="python")

        st.caption("결과")
        st.code(
            "15\n5\n50\n2.0\n0\n100000\n2",
            language="text"
        )

    # 비교 연산자
    with st.expander("비교 연산자"):
        st.caption("두 값을 비교해 True 또는 False를 반환하는 연산자")
        st.dataframe({
            "연산자": ["==", "!=", ">", "<", ">=", "<="],
            "의미": ["같다", "같지 않다", "크다", "작다", "크거나 같다", "작거나 같다"],
        })

        st.caption("실습 예제")
        st.code(textwrap.dedent("""
        a = 10
        b = 5

        print(a == b)
        print(a != b)
        print(a > b)
        print(a < b)
        print(a >= b)
        print(a <= b) 
        """),
        language="python")    

        st.caption("결과")
        st.code(
            "False\nTrue\nTrue\nFalse\nTrue\nFalse",
            language="text"
        )

    # 논리 연산자
    with st.expander("논리 연산자"):
        st.caption("여러 조건을 조합하거나 조건을 반대로 만들 때 사용하는 연산자")
        st.dataframe({
            "연산자": ["and", "or", "not"],
            "의미": ["그리고", "또는", "아니다"],
        })
        st.caption("실습 예제")
        st.code(
            textwrap.dedent("""
            a = 10
            b = 5

            # 두 조건이 모두 참이면 True
            print(a > 5 and b < 10) 

            # 하나의 조건이라도 참이면 True
            print(a > 15 or b < 10) 

            # 조건의 결과를 반대로 변경
            print(not a < 5)
            """),
            language="python"
        )
        st.caption("결과")
        st.code(
            "True\nTrue\nTrue",
            language="text"
        )

    # 대입 연산자
    with st.expander("대입 연산자"):
        st.caption("변수에 값을 저장하거나 기존 값에 연산한 결과를 다시 저장")
        st.dataframe({
            "연산자": ["=", "+=", "-=", "*=", "/="],
            "의미": ["대입", "더해서 대입", "빼서 대입", "곱해서 대입", "나눠서 대입"],
        })
        st.caption("실습 예제")
        st.caption("일반적인 대입문 `=`은 `print()`에서 직접 사용할 수 없음")
        st.code(
            textwrap.dedent("""
            a = 10
            b = 5

            # a에 b를 더한 값을 다시 a에 저장
            a += b
            print(a)

            # a에서 b를 뺀 값을 다시 a에 저장
            a -= b
            print(a)

            # a에 b를 곱한 값을 다시 a에 저장
            a *= b
            print(a)

            # a를 b로 나눈 값을 다시 a에 저장
            a /= b
            print(a)
            """),
            language="python"
        )
        st.caption("결과")
        st.code(
            "15\n10\n50\n10.0",
            language="text"
        )


    # 포함 연산자
    with st.expander("포함 연산자"):
        st.caption("특정 값이 데이터 안에 포함되어 있는지 확인")
        st.dataframe({
            "연산자": ["in", "not in"],
            "의미": ["포함", "미포함"],
        })
        st.caption("실습 예제")
        st.code(
            textwrap.dedent("""
            fruits = ["사과", "바나나", "포도"]

            # 리스트에 사과가 포함되어 있는지 확인
            print("사과" in fruits)

            # 리스트에 수박이 포함되어 있는지 확인
            print("수박" in fruits)

            # 리스트에 수박이 포함되어 있지 않은지 확인
            print("수박" not in fruits)

            # 리스트에 사과가 포함되어 있지 않은지 확인
            print("사과" not in fruits)
            """),
            language="python"
        )
        st.caption("결과")
        st.code(
            "True\nFalse\nTrue\nFalse",
            language="text"
        )

    # 조건문
    st.markdown(":violet-badge[조건문] 사용 방법")

    with st.expander("if문"):
        st.caption("조건이 참일 때 코드를 실행")
        st.code(
            textwrap.dedent("""
                age = 20

                # 조건이 참일 때 실행
                if age >= 18:
                    print("성인입니다.")
            """),
            language="python"
        )
        st.caption("결과")
        st.code("성인입니다.", language="text")

    with st.expander("if ~ else문"):
        st.caption("조건이 참이면 if를, 거짓이면 else를 실행")
        st.code(
            textwrap.dedent("""
            age = 15

            if age >= 18:   # age가 18 이상이면 if 실행
                print("성인입니다.")
            
            else:   # 조건이 거짓이면 else 실행
                print("미성년자입니다.")
            """),
            language="python"
        )
        st.caption("결과")
        st.code("미성년자입니다.", language="text")
        
    with st.expander("if ~ elif ~ else문"):
        st.caption("여러 조건을 순서대로 확인하고 해당하는 코드를 실행")
        st.code(
            textwrap.dedent("""
            score = 85
            
            if score >= 90:     # 90점 이상이면 A
                print("A")
            elif score >= 80:   # 80점 이상이면 B
                print("B")
            else:   # 위 조건에 모두 해당하지 않으면 C
                print("C")
            """),
            language="python"
        )

        st.caption("결과")
        st.code("B", language="text")        

    # 반복문
    st.markdown(":violet-badge[반복문] 사용 방법")

    with st.expander("for문"):
        st.caption("리스트나 시퀀스의 값을 하나씩 꺼내 반복")
        st.code(
            textwrap.dedent("""
            fruits = ["사과", "바나나", "포도"]

            for fruit in fruits: # 리스트의 값을 하나씩 꺼내 반복
                print(fruit)
            """),
            language="python"
        )
        st.caption("결과")
        st.code("사과\n바나나\n포도", language="text")

    with st.expander("for문 + range()"):
        st.caption("range()로 만든 숫자 범위를 이용해 반복")
        st.code(
            textwrap.dedent("""
            # 0부터 4까지 숫자를 생성해 반복
            for i in range(5):
                print(i)

            # range(5) → 0부터 4까지
            """),
            language="python"            
        )
        st.caption("결과")
        st.code("0\n1\n2\n3\n4", language="text")

    with st.expander("while문"):
            st.caption("조건이 참인 동안 코드를 계속 반복")
            st.code(
                textwrap.dedent("""
                count = 1

                while count <= 3:   # count가 3 이하인 동안 반복
                    print(count)

                    count += 1  # count를 1씩 증가
                """),
                language="python"
            )
            st.caption("결과")
            st.code("1\n2\n3", language="text")

    with st.expander("break문"):
        st.caption("반복문을 즉시 종료")
        st.code(
            textwrap.dedent("""
            for i in range(5):
                if i == 3:  # i가 3이면 반복문 전체 종료
                    break

                print(i)
            """),
            language="python"
        )
        st.caption("결과")
        st.code("0\n1\n2", language="text")

    with st.expander("continue문"):
        st.caption("현재 반복만 건너뛰고 다음 반복으로 이동")
        st.code(
            textwrap.dedent("""
            for i in range(5):
                if i == 2: # i가 2이면 현재 반복만 건너뜀
                    continue

                print(i)
            """),
            language="python"
        )
        st.caption("결과")
        st.code("0\n1\n3\n4", language="text")

    st.markdown(":violet-badge[종합 실습]")

    with st.expander("실습 예제"):
        st.code(
            textwrap.dedent("""
            questions = ["asyncio란?", "", "FastAPI란?"]
            valid_questions: list[str] = []

            # questions의 값을 하나씩 확인
            for question in questions:

                # 문자열 양쪽의 공백 제거
                cleaned = question.strip()

                # 빈 문자열이면 다음 반복으로 이동
                if not cleaned:
                    continue

                # 유효한 질문만 리스트에 추가
                valid_questions.append(cleaned)

            print(valid_questions)
            """),
            language="python"
        )

        st.caption("결과")
        st.code("['asyncio란?', 'FastAPI란?']", language="text")

    st.divider()