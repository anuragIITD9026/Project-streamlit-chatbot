import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://wallpaperaccess.com/full/1567679.jpg");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# load_dotenv()
# st.set_page_config(
#     page_title="Chatbot",
#     page_icon=":brain:",
#     layout="centered"
# )
st.set_page_config(page_title="Chatbot", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpaperaccess.com/full/1567679.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
    /* Chat container background fix */
    .block-container {
        padding-top: 2rem;
        background-color: rgba(0, 0, 0, 0.4);
        border-radius: 15px;
    }

    /* Chat message style */
    div.stChatMessage {
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: white !important;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* Input box styling */
    textarea {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: white !important;
        border-radius: 10px;
        border: 1px solid #666 !important;
    }

    /* Button styling */
    button[kind="primary"] {
        background-color: rgba(0,0,0,0.4) !important;
        color: white !important;
        border: 1px solid #666 !important;
    }

    /* Fix black box under chat input */
    .css-1y4p8pa {
        background-color: transparent !important;
        box-shadow: none !important;
    }

    /* Optional: frosted glass input wrapper */
    .css-1gulkj5 {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border-radius: 8px;
        padding: 10px;
        backdrop-filter: blur(5px);
    }

    /* Title & heading colors */
    h1, h2, h3, p {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title(":brain: Gemini Chatbot")

GOOGLE_API_KEY=os.getenv(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

def translate_role_for_streamlit(user_role):
    if user_role=='model':
        return "assistant"
    else:
        return user_role
if "chat_session" not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])
st.title("chatbot")
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
user_prompt=st.chat_input("Ask Chatbot ...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    chatbot_response=st.session_state.chat_session.send_message(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(chatbot_response.text)
