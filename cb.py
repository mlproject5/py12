import streamlit as st
import requests


st.set_page_config(page_title='ChatBot', page_icon='chatbot.png', layout="centered", initial_sidebar_state="auto",
                   menu_items=None)

API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def generate_response(message):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>ChatBot Demo</h1></center>",
            unsafe_allow_html=True)

user_input = st.text_area("User Question")

if st.button("Send"):
    response = generate_response(user_input)
    st.text_area("ChatBot Answer", value=response, height=200, max_chars=None)
