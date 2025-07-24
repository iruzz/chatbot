import streamlit as st
from main import chat_inference

# Konfigurasi halaman
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .user-bubble {
            background-color: #d1e7dd;
            color: #000;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: right;
        }

        .bot-bubble {
            background-color: #f8d7da;
            color: #000;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
        }

        .chat-container {
            padding: 10px;
        }

        .title {
            font-size: 32px;
            font-weight: bold;
            color: #2b5876;
            margin-bottom: 10px;
        }

        .subtext {
            color: #666;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Judul dan deskripsi
st.markdown('<div class="title">🤖 Gemini Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Chatbot sederhana menggunakan Gemini API</div>', unsafe_allow_html=True)

# Inisialisasi session state untuk pesan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan pesan sebelumnya
with st.container():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-bubble">🧑 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-bubble">🤖 {message["content"]}</div>', unsafe_allow_html=True)

# Input chat
prompt = st.chat_input("Ketik pesan kamu di sini...")

if prompt:
    # Tampilkan pesan user
    st.markdown(f'<div class="user-bubble">🧑 {prompt}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Proses dan tampilkan balasan bot
    with st.spinner("Sedang mengetik..."):
        response = chat_inference(prompt)

    st.markdown(f'<div class="bot-bubble">🤖 {response}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})
