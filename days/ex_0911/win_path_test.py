from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model = "gpt-5-mini",
    input = "연결 테스트, '연결 성공'으로 대답"
)

print(response.output_text)

