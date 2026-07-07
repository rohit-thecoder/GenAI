import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="My Funny AI Agent", page_icon="🤖")
st.title("🤖 Funny AI ChatBot")

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.9,
    api_key=os.getenv("MISTRAL_API_KEY")
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are my Funny AI Agent")
    ]

# Display previous messages (skip the SystemMessage)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input
prompt = st.chat_input("Ask Anything")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)