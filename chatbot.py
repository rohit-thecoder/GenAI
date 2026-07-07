import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest", temperature=0.9,
    api_key=os.getenv("MISTRAL_API_KEY")  # Optional if already in .env
)

messages = [
    SystemMessage(content = "You are my Funny AI Agent")
]

print("----Welcome to My ChatBot (0 to EXIT!)----")
while True:
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    messages.append(prompt)
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:" ,response.content)

print(messages)