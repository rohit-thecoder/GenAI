import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest", temperature=0.9,max_tokens=20,
    api_key=os.getenv("MISTRAL_API_KEY")  # Optional if already in .env
)

response = model.invoke("Write a poem on AI")
print(response.content)