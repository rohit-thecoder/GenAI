import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest", temperature=0.9,
    api_key=os.getenv("MISTRAL_API_KEY")  # Optional if already in .env
)

print("Choose Your AI Mode")
print("Type 1 for Angry Mode")
print("Type 2 for Sad Mode")
print("Type 3 for Sad Mode")
choice = int(input("Tell Your Response: "))

if choice == 1:
    mode = "You are an angry AI Agent. You respond Aggressively and impatiently"
elif choice == 2:
    mode = "You are an Funny AI Agent. You respond with humor and jokes"
elif choice == 3:
    mode = "You and an Sad AI Agent. You respond in sad way "    



messages = [
    SystemMessage(content = mode)
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