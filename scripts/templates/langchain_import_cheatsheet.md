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

## 모델 (Chat Models)

| Import | 설명 |
|---|---|
| from langchain.chat_models import init_chat_model | provider 이름만 바꿔서 여러 LLM을 통일된 방식으로 초기화 |
| from langchain_openai import ChatOpenAI | OpenAI 전용 채팅모델 클래스 |
| from langchain_openai import OpenAIEmbeddings | OpenAI 임베딩 클래스 |
| from langchain_anthropic import ChatAnthropic | Anthropic(Claude) 전용 채팅모델 클래스 |
| from langchain_google_genai import ChatGoogleGenerativeAI | Google Gemini 전용 채팅모델 클래스 |
| from langchain_community.chat_models import ChatOllama | 로컬 Ollama 모델 실행용 채팅모델 클래스 |
| from langchain_core.language_models import BaseChatModel | 커스텀 채팅모델을 만들 때 상속하는 기본 클래스 |

## 프롬프트 (Prompts)

| Import | 설명 |
|---|---|
| from langchain_core.prompts import PromptTemplate | 단일 문자열 프롬프트 템플릿 |
| from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder | 채팅형 프롬프트 + 대화 히스토리 자리표시자 |
| from langchain_core.prompts import FewShotPromptTemplate | 예시(few-shot)를 넣는 문자열 프롬프트 |
| from langchain_core.prompts import FewShotChatMessagePromptTemplate | 예시를 넣는 채팅형 프롬프트 |
| from langchain_core.prompts import load_prompt | yaml/json 파일에서 프롬프트 불러오기 |
| from langchain_core.prompts.few_shot import FewShotPromptTemplate | 위 FewShotPromptTemplate과 동일(하위 모듈 경로) |
| from langchain import hub | LangChain Hub에서 공유 프롬프트 템플릿 가져오기(`hub.pull(...)`) |

## 메시지 (Messages)

| Import | 설명 |
|---|---|
| from langchain_core.messages import SystemMessage, HumanMessage, AIMessage | 시스템/사용자/AI 발화 메시지 객체 |
| from langchain.messages import SystemMessage, HumanMessage | langchain 패키지에서 재노출된 동일 클래스(별칭) |
| from langchain_core.messages import ToolMessage | 툴 실행 결과를 담아 모델에 되돌려주는 메시지 객체 |
| from langchain_core.messages import trim_messages | 토큰 한도에 맞춰 대화 메시지 목록을 잘라내는 유틸 |

## 출력 파서 (Output Parsers)

| Import | 설명 |
|---|---|
| from langchain_core.output_parsers import StrOutputParser | LLM 출력을 순수 문자열로 파싱 |
| from langchain_core.output_parsers import JsonOutputParser | 출력을 JSON(dict)으로 파싱 |
| from langchain_core.output_parsers import PydanticOutputParser | 출력을 Pydantic 모델 객체로 파싱 |
| from langchain_core.output_parsers import CommaSeparatedListOutputParser | "a, b, c" → 리스트로 파싱 |
| from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema | 필드 스키마 기반 구조화 출력 파싱(구버전 스타일) |
| from langchain_classic.output_parsers import EnumOutputParser | 정해진 열거값(Enum) 중 하나로 파싱 (langchain-classic으로 이동) |
| from langchain_classic.output_parsers import DatetimeOutputParser | 날짜/시간 문자열로 파싱 (langchain-classic으로 이동) |
| from langchain_classic.output_parsers import PandasDataFrameOutputParser | DataFrame 조회 결과로 파싱 (langchain-classic으로 이동) |

## Runnable (LCEL)

| Import | 설명 |
|---|---|
| from langchain_core.runnables import RunnablePassthrough | 입력을 그대로(또는 일부 가공해) 다음 단계로 전달 |
| from langchain_core.runnables import RunnableParallel | 여러 체인을 동시에 실행해 결과를 dict로 합침 |
| from langchain_core.runnables import RunnableBranch | 조건에 따라 다른 체인으로 분기 |
| from langchain_core.runnables import RunnableLambda | 일반 파이썬 함수를 체인 구성요소로 감싸기 |
| from langchain_core.runnables import RunnableConfig | 체인 실행 시 콜백/태그/메타데이터 등을 전달하는 설정 객체 |
| from langchain_core.runnables.history import RunnableWithMessageHistory | 체인에 대화 히스토리(메모리) 자동 관리 기능 부여 |
| from langchain_core.runnables import ConfigurableField | 실행 시점에 체인의 파라미터(모델명 등)를 바꿀 수 있게 설정 |

## 문서 로더 (Document Loaders)

| Import | 설명 |
|---|---|
| from langchain_community.document_loaders import PyPDFLoader | PDF 파일을 문서(Document) 목록으로 로드 |
| from langchain_community.document_loaders import TextLoader | 일반 텍스트 파일 로드 |
| from langchain_community.document_loaders import CSVLoader | CSV 파일을 행 단위 문서로 로드 |
| from langchain_community.document_loaders import WebBaseLoader | 웹페이지 URL을 크롤링해 문서로 로드 |
| from langchain_community.document_loaders import UnstructuredWordDocumentLoader | Word(docx) 문서 로드 |
| from langchain_community.document_loaders import DirectoryLoader | 폴더 내 여러 파일을 한 번에 로드 |

## 텍스트 분할 (Text Splitters)

| Import | 설명 |
|---|---|
| from langchain_text_splitters import RecursiveCharacterTextSplitter | 문단/문장 단위로 재귀적으로 쪼개는 가장 널리 쓰이는 분할기 |
| from langchain_text_splitters import CharacterTextSplitter | 단순 구분자 기준 텍스트 분할기 |
| from langchain_text_splitters import TokenTextSplitter | 토큰 개수 기준으로 텍스트 분할 |
| from langchain_text_splitters import MarkdownHeaderTextSplitter | 마크다운 헤더(#, ##) 기준으로 문서 분할 |

## 문서 / 벡터스토어 / 임베딩 (RAG)

| Import | 설명 |
|---|---|
| from langchain_core.documents import Document | 텍스트 + 메타데이터를 담는 기본 문서 객체 |
| from langchain_openai import OpenAIEmbeddings | 텍스트를 벡터로 변환(OpenAI 임베딩 모델) |
| from langchain_huggingface import HuggingFaceEmbeddings | HuggingFace 오픈소스 임베딩 모델 사용 |
| from langchain_community.vectorstores import FAISS | 로컬 인메모리 벡터스토어 |
| from langchain_chroma import Chroma | Chroma 벡터스토어 |
| from langchain_pinecone import PineconeVectorStore | Pinecone 클라우드 벡터스토어(실무에서 자주 사용) |
| from langchain_core.example_selectors import SemanticSimilarityExampleSelector | 질문과 의미적으로 유사한 few-shot 예시 선택 |
| from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector | 유사도 + 다양성을 함께 고려해 예시 선택 |
| from langchain.retrievers import ContextualCompressionRetriever | 검색 결과를 재압축/재랭킹해 관련성 높은 부분만 반환 |
| from langchain.retrievers.multi_query import MultiQueryRetriever | 질문을 여러 관점으로 재작성해 검색 재현율 향상 |
| from langchain_community.retrievers import BM25Retriever | 키워드 기반(BM25) 검색기, 벡터검색과 하이브리드로 자주 사용 |

## 메모리 (Memory)

| Import | 설명 |
|---|---|
| from langchain.memory import ConversationBufferMemory | 대화 내용을 그대로 버퍼에 저장하는 메모리(구버전 스타일) |
| from langchain.memory import ConversationSummaryMemory | 대화가 길어지면 요약해서 저장하는 메모리 |
| from langchain_community.chat_message_histories import ChatMessageHistory | 세션별 대화 히스토리 저장소(RunnableWithMessageHistory와 함께 사용) |

## 에이전트 / 툴

| Import | 설명 |
|---|---|
| from langchain_core.tools import tool | 일반 함수를 LLM이 호출할 수 있는 Tool로 변환하는 데코레이터 |
| from langchain.agents import create_agent | LLM + 툴 목록으로 에이전트 생성 |
| from langchain_core.tools import StructuredTool | 여러 인자를 받는 함수를 스키마 기반 Tool로 변환 |
| from langchain_community.tools import DuckDuckGoSearchRun | 실무에서 자주 쓰는 웹 검색 툴 |
| from langchain_community.utilities import SQLDatabase | SQL DB 연결/쿼리용 유틸(SQL 에이전트 구성에 사용) |
| from langgraph.graph import StateGraph, END | 상태 기반 에이전트/워크플로우 그래프 구성(최신 에이전트 표준) |
| from langgraph.checkpoint.memory import MemorySaver | LangGraph 실행 상태를 체크포인트로 저장(대화 지속성) |
| from langgraph.prebuilt import create_react_agent | ReAct 패턴 에이전트를 즉시 생성하는 프리셋 |

## 캐시 / 직렬화 / 콜백 / 기타 유틸

| Import | 설명 |
|---|---|
| from langchain_community.cache import SQLiteCache | LLM 응답을 SQLite 파일에 캐싱 |
| from langchain_core.globals import set_llm_cache | 전역 LLM 캐시 설정(위 SQLiteCache 등록용) |
| from langchain_core.load import dumpd, dumps | LangChain 객체를 dict/JSON 문자열로 직렬화 |
| from langchain_core.callbacks import BaseCallbackHandler | 체인/모델 실행 이벤트(토큰, 시작/종료 등)를 감지하는 콜백 핸들러 |
| from langchain_community.callbacks import get_openai_callback | OpenAI 호출 비용/토큰 사용량 추적(실무 모니터링에 자주 사용) |
| from langchain_core.tracers.langchain import wait_for_all_tracers | LangSmith 트레이싱이 끝날 때까지 대기 |

---

### 미리보기 팁
파일 열고 `Ctrl+Shift+V` (또는 우측 상단 미리보기 아이콘)로 렌더링해서 보면 편함.
