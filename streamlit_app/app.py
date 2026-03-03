import streamlit as st
import requests

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AI Agent System",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# Custom CSS for AI Look
# -------------------------
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: white;
    }

    .chat-container {
        max-width: 800px;
        margin: auto;
    }

    .user-bubble {
        background-color: #2563eb;
        padding: 12px 16px;
        border-radius: 18px;
        margin-bottom: 10px;
        color: white;
        width: fit-content;
        margin-left: auto;
    }

    .ai-bubble {
        background-color: #1f2937;
        padding: 12px 16px;
        border-radius: 18px;
        margin-bottom: 10px;
        color: white;
        width: fit-content;
        margin-right: auto;
    }

    .title-style {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------
st.markdown('<div class="title-style">🤖 AI Multi-Agent System</div>', unsafe_allow_html=True)

# -------------------------
# Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Chat Input
# -------------------------
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking like an AI agent... 🧠"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/ask/",
                json={"question": user_input}
            )
            data = response.json()

            answer = data.get("answer", "No answer found.")
            plan = data.get("plan", "")
            
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "plan": plan
            })

        except Exception as e:
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Error connecting to backend: {e}",
                "plan": ""
            })

# -------------------------
# Display Chat Messages
# -------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

    else:
        st.markdown(f'<div class="ai-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

        if msg.get("plan"):
            with st.expander("🧠 Agent Thinking Process"):
                st.write("**Planner Decision:**")
                st.write(msg["plan"])