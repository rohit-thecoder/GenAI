from dotenv import load_dotenv
import os

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")
print(response.content)