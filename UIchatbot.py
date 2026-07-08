import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="AI ChatBot", page_icon="🤖")

st.title("🤖 Multi Mode AI ChatBot")

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.9,
    api_key=os.getenv("MISTRAL_API_KEY")
)

# ---------------- AI Modes ---------------- #

modes = {
    "😡 Angry": "You are an angry AI.",
    "😂 Funny": "You are a comedian AI.",
    "😢 Sad": "You are a sad AI.",
    "❤️ Romantic": "You are a romantic AI.",
    "🤓 Teacher": "You are an expert teacher.",
    "💼 Professional": "You are a professional business consultant.",
    "👨‍💻 Programmer": "You are an expert software engineer.",
    "🧘 Motivational": "You are a motivational life coach.",
    "👑 Roast King": "Roast everyone in a funny way without being offensive."
}

selected_mode = st.sidebar.selectbox(
    "Choose AI Mode",
    list(modes.keys())
)

# --------------- Initialize Session ---------------- #

if "current_mode" not in st.session_state:
    st.session_state.current_mode = selected_mode

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=modes[selected_mode])
    ]

# If user changes mode
if selected_mode != st.session_state.current_mode:
    st.session_state.current_mode = selected_mode

    # Reset conversation with new SystemMessage
    st.session_state.messages = [
        SystemMessage(content=modes[selected_mode])
    ]

    st.success(f"Mode changed to {selected_mode}")

# ---------------- Display Chat ---------------- #

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---------------- Chat Input ---------------- #

prompt = st.chat_input("Ask Anything...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)