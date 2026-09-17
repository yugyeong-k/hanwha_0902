# LangChain Import 치트시트

> `requirements.txt` 기준 버전: langchain 1.4.1 / langchain-core 1.6.3 / langchain-community 0.4.2 / langchain-classic 1.0.8

## 호출 가능한 모델 (2026-09 기준, `init_chat_model` provider)

| Provider | 모델 | 특징 | 컨텍스트/최대 출력 토큰 |
|---|---|---|---|
| openai | gpt-4o / gpt-4o-mini | 멀티모달, 범용 균형형 | 128K / 16K 출력 |
| openai | gpt-4.1 / gpt-4.1-mini | 긴 컨텍스트, 코딩 강화 | 1M / 32K 출력 |
| anthropic | claude-opus-5 | 최고 성능, 복잡한 추론·에이전트용 | 200K (확장 시 1M) |
| anthropic | claude-sonnet-5 | 성능·속도·비용 균형, 기본 추천 | 200K (확장 시 1M) |
| anthropic | claude-haiku-4-5 | 저지연·저비용, 대량 처리용 | 200K |
| google_genai | gemini-3.5-pro | 최상위 추론, 초장문 컨텍스트 | 2M |
| google_genai | gemini-3.5-flash | 빠르고 저렴, 대용량 처리 | 1M |

> `model_provider` 값만 바꾸면 `init_chat_model(model, model_provider=...)`로 동일 인터페이스 사용 가능. 토큰 한도·모델명은 공급사 업데이트로 자주 바뀌므로 실제 사용 전 공식 문서로 재확인 권장.

## 설치

```bat
..\..\scripts\setup.bat rag chroma
```

## 환경 확인 (버전/키 체크)

```python
import os
import sys
import langchain          # 버전 확인용 (langchain.__version__)
import langchain_core     # 버전 확인용 (langchain_core.__version__)
import langchain_openai   # 버전 확인용 (langchain_openai.__version__)
from dotenv import load_dotenv  # .env 파일에서 API 키 등 환경변수 로드

load_dotenv()
```

## 모델 (Chat Models)

```python
from langchain.chat_models import init_chat_model   # provider 이름만 바꿔서 여러 LLM을 통일된 방식으로 초기화
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # OpenAI 전용 채팅모델 / 임베딩 클래스
```

```python
# provider별 LLM 초기화 (model_provider만 바꾸면 동일한 인터페이스로 사용 가능)
openai_llm = init_chat_model("gpt-4o-mini", model_provider="openai", temperature=0, max_tokens=2048)
anthropic_llm = init_chat_model("claude-3-5-haiku-latest", model_provider="anthropic", temperature=0, max_tokens=2048)
google_llm = init_chat_model("gemini-3.5-flash", model_provider="google_genai", temperature=0, max_tokens=2048)
```

## 프롬프트 (Prompts)

```python
from langchain_core.prompts import PromptTemplate            # 단일 문자열 프롬프트 템플릿
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # 채팅형 프롬프트 + 대화 히스토리 자리표시자
from langchain_core.prompts import FewShotPromptTemplate      # 예시(few-shot)를 넣는 문자열 프롬프트
from langchain_core.prompts import FewShotChatMessagePromptTemplate  # 예시를 넣는 채팅형 프롬프트
from langchain_core.prompts import load_prompt                # yaml/json 파일에서 프롬프트 불러오기
from langchain_core.prompts.few_shot import FewShotPromptTemplate  # 위 FewShotPromptTemplate과 동일(하위 모듈 경로)
```

## 메시지 (Messages)

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  # 시스템/사용자/AI 발화 메시지 객체
from langchain.messages import SystemMessage, HumanMessage  # langchain 패키지에서 재노출된 동일 클래스(별칭)
```

## 출력 파서 (Output Parsers)

```python
from langchain_core.output_parsers import StrOutputParser       # LLM 출력을 순수 문자열로 파싱
from langchain_core.output_parsers import JsonOutputParser       # 출력을 JSON(dict)으로 파싱
from langchain_core.output_parsers import PydanticOutputParser   # 출력을 Pydantic 모델 객체로 파싱
from langchain_core.output_parsers import CommaSeparatedListOutputParser  # "a, b, c" → 리스트로 파싱

# langchain-classic 쪽으로 이동한 파서들 (v1에서 core 밖으로 분리됨)
from langchain_classic.output_parsers import EnumOutputParser         # 정해진 열거값(Enum) 중 하나로 파싱
from langchain_classic.output_parsers import DatetimeOutputParser     # 날짜/시간 문자열로 파싱
from langchain_classic.output_parsers import PandasDataFrameOutputParser  # DataFrame 조회 결과로 파싱
```

## Runnable (LCEL)

```python
from langchain_core.runnables import RunnablePassthrough  # 입력을 그대로(또는 일부 가공해) 다음 단계로 전달
from langchain_core.runnables import RunnableParallel      # 여러 체인을 동시에 실행해 결과를 dict로 합침
from langchain_core.runnables import RunnableBranch        # 조건에 따라 다른 체인으로 분기
from langchain_core.runnables import RunnableLambda        # 일반 파이썬 함수를 체인 구성요소로 감싸기
```

## 문서 / 벡터스토어 / 임베딩 (RAG)

```python
from langchain_core.documents import Document           # 텍스트 + 메타데이터를 담는 기본 문서 객체
from langchain_openai import OpenAIEmbeddings            # 텍스트를 벡터로 변환(OpenAI 임베딩 모델)
from langchain_community.vectorstores import FAISS       # 로컬 인메모리 벡터스토어
from langchain_chroma import Chroma                      # Chroma 벡터스토어
from langchain_core.example_selectors import (
    SemanticSimilarityExampleSelector,      # 질문과 의미적으로 유사한 few-shot 예시 선택
    MaxMarginalRelevanceExampleSelector,    # 유사도 + 다양성을 함께 고려해 예시 선택
)
```

## 에이전트 / 툴

```python
from langchain_core.tools import tool          # 일반 함수를 LLM이 호출할 수 있는 Tool로 변환하는 데코레이터
from langchain.agents import create_agent       # LLM + 툴 목록으로 에이전트 생성
```

## 캐시 / 직렬화 / 기타 유틸

```python
from langchain_community.cache import SQLiteCache   # LLM 응답을 SQLite 파일에 캐싱
from langchain_core.globals import set_llm_cache    # 전역 LLM 캐시 설정(위 SQLiteCache 등록용)
from langchain_core.load import dumpd, dumps        # LangChain 객체를 dict/JSON 문자열로 직렬화
```

---

### 미리보기 팁
파일 열고 `Ctrl+Shift+V` (또는 우측 상단 미리보기 아이콘)로 렌더링해서 보면 편함.
