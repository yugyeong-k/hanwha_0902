import streamlit as st
import textwrap


def show():

    st.title("Day 03", icon="📖")
    st.caption("2026년 09월 04일")
    st.divider()

    # 1. Streamlit
    st.markdown("### 1. Streamlit")
    st.caption("Streamlit 공식 문서 및 기능 참고")

    st.markdown(":violet-badge[바로가기]")

    with st.container(horizontal=True):
        st.link_button(
            "공식 사이트",
            "https://streamlit.io/",
            width="content"
        )

        st.link_button(
            "개발 문서",
            "https://docs.streamlit.io/",
            width="content"
        )

        st.link_button(
            "기능 참고",
            "https://docs.streamlit.io/develop/api-reference",
            width="content"
        )

        st.link_button(
            "다중 페이지 구성",
            "https://docs.streamlit.io/develop/tutorials/multipage/dynamic-navigation",
            width="content"
        )

    # 2. GitHub
    st.markdown("### 2. GitHub")
    st.caption("Git과 GitHub를 이용한 코드 관리 및 버전 관리")

    st.markdown(":violet-badge[GitHub 기초]")
    with st.expander("Git · GitHub · GitHub Desktop"):
        st.markdown("""
        - :blue-badge[Git] : 코드의 변경 이력을 관리하는 버전 관리 도구
        - :blue-badge[GitHub] : Git 저장소를 온라인에서 관리하는 서비스
        - :blue-badge[GitHub Desktop] : Git을 GUI 환경에서 쉽게 사용하는 프로그램
        """)

    with st.expander("GitHub Desktop 설치 및 저장소 연결"):
        st.markdown("""
        1. **:blue-badge[GitHub Desktop]** 설치
            - 프로그램 설치
            - GitHub 계정으로 로그인 및 연결

        2. **:blue-badge[Repository(저장소)]** 생성
            - GitHub에서 새로운 저장소 생성
            - 저장소 이름 및 공개 여부 설정

        3. **:blue-badge[GitHub Desktop]** 에서 저장소 선택
            - 생성한 저장소 선택
            - 로컬 저장소 위치 설정

        4. **:blue-badge[로컬 프로젝트]** 와 **:blue-badge[저장소]** 연결
            - 프로젝트 폴더 연결
            - 연결된 프로젝트를 Git으로 관리
        """)

    with st.expander("Commit · Push"):
        st.caption("변경 내용을 기록하고 GitHub에 업로드")
        st.markdown("""
        
        - :blue-badge[Commit] : 변경된 작업 내용을 기록
        - :blue-badge[Push] : Commit한 내용을 GitHub에 업로드
        """)

        st.code(
            textwrap.dedent("""
            프로젝트 수정
                ↓
            변경 사항 확인
                ↓
              Commit --- 변경 내용 기록
                ↓
               Push  --- GitHub에 업로드
                ↓
            GitHub에서 확인
            """),
            language="text"
        )

    st.divider()

    # 3. Python 기본 문법
    st.markdown("### 3. Python 기본 문법")
    st.caption("W3Schools로 Python 기본 문법 학습")

    # f-string
    st.markdown(":violet-badge[f-string] 사용 방법")

    with st.expander("실습 예제"):
        st.caption("문자열 안에 변수의 값을 넣어 출력")
        st.code(
            textwrap.dedent("""
            age = 36

            txt = f"age : {age}"
            print(txt)

            txt2 = f"age : {age:.2f}"
            print(txt2)
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            age : 36
            age : 36.00
            """),
            language="text"
        )

    # 문자열 메서드
    st.markdown(":violet-badge[문자열 메서드] 사용 방법")

    with st.expander("실습 예제"):

        st.code(
            textwrap.dedent("""
            # 문자열 가운데 정렬
            txt = "banana"
            print(txt.center(20))

            # 특정 문자열의 위치 찾기
            txt2 = "Hello, welcome to my world."
            print(txt2.find("welcome"))

            # 대문자로 구성되어 있는지 확인
            txt3 = "THIS IS NOW!"
            print(txt3.isupper())

            # 왼쪽 공백 제거
            txt4 = "     banana     "
            x = txt4.lstrip()
            print("of all fruits", x, "is my favorite")

            # 특정 문자 변경
            txt5 = "Hello Sam!"
            mytable = str.maketrans("S", "P")
            print(txt5.translate(mytable))
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
                         banana
            7
            True
            of all fruits banana      is my favorite
            Hello Pam!
            """),
            language="text"
        )

    # 딕셔너리 메서드
    st.markdown(":violet-badge[딕셔너리 메서드] 사용 방법")

    with st.expander("실습 예제"):

        st.code(
            textwrap.dedent("""
            car = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
            }

            # 딕셔너리의 키 확인
            x = car.keys()
            print(x)

            # 새로운 키와 값 추가
            car["color"] = "white"
            print(x)

            # 딕셔너리의 값 확인
            y = car.values()
            print(y)

            print(car)
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            dict_keys(['brand', 'model', 'year'])
            dict_keys(['brand', 'model', 'year', 'color'])
            dict_values(['Ford', 'Mustang', 1964, 'white'])
            {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
            """),
            language="text"
        )

    st.divider()

    # 4. NumPy
    st.markdown("### 4. NumPy")
    st.caption("Python에서 배열을 다루기 위한 라이브러리")

    # NumPy 배열
    st.markdown(":violet-badge[NumPy 배열] 생성 방법")

    with st.expander("실습 예제"):

        st.code(
            textwrap.dedent("""
            import numpy as np

            arr = np.array([1, 2, 3])

            print(arr)
            print(type(arr))
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            [1 2 3]
            <class 'numpy.ndarray'>
            """),
            language="text"
        )

    # 배열 차원
    st.markdown(":violet-badge[배열 차원]")

    with st.expander("0차원 · 1차원 · 2차원 · 3차원"):

        st.code(
            textwrap.dedent("""
            import numpy as np

            # 0차원
            arr0 = np.array(100)

            # 1차원
            arr1 = np.array([1, 2, 3])

            # 2차원 [행, 열]
            arr2 = np.array([
                [1, 2, 3],
                [4, 5, 6]
            ])

            # 3차원 [면, 행, 열]
            arr3 = np.array([
                [
                    [1, 2, 3],
                    [4, 5, 6]
                ],
                [
                    [1, 2, 3],
                    [4, 5, 6]
                ]
            ])
            """),
            language="python"
        )

    # ndim
    st.markdown(":violet-badge[ndim] 사용 방법")

    with st.expander("배열의 차원 수 확인"):

        st.caption("`ndim`으로 배열의 차원 수를 확인")

        st.code(
            textwrap.dedent("""
            print(arr1.ndim)
            print(arr2.ndim)
            print(arr3.ndim)
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            1
            2
            3
            """),
            language="text"
        )

    # ndmin
    st.markdown(":violet-badge[ndmin] 사용 방법")

    with st.expander("배열의 최소 차원 수 지정"):

        st.caption("`ndmin`으로 배열의 최소 차원 수를 지정")

        st.code(
            textwrap.dedent("""
            arr5 = np.array([1, 2, 3, 4], ndmin=5)

            print(arr5)
            print(arr5.ndim)
            """),
            language="python"
        )

        st.caption("결과")

        st.code(
            textwrap.dedent("""
            [[[[[1 2 3 4]]]]]
            5
            """),
            language="text"
        )

    st.divider()