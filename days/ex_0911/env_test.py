import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model = "gpt-5-mini",
    input = "연결 테스트, '연결 성공'으로 대답"
)

print(response.output_text)