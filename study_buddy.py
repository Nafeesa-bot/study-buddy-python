# study_buddy.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


# ---------- BASIC SETUP ----------
# Global variable (shows GLOBAL SCOPE)
history = []  # List to store chat history (LIST + DICT usage)

# Configure API key (VARIABLE + ASSIGNMENT)
# Put your Gemini API key in an environment variable before running:
# export GEMINI_API_KEY="your_api_key"
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# ---------- FUNCTION DEFINITIONS ----------
def ask_gemini(prompt, model="gemini-2.5-flash"):
    """Function to ask Gemini a question and return answer (FRUITFUL FUNCTION)"""
    chat = genai.GenerativeModel(model).start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text


def add_to_history(question, answer):
    """Function to store Q&A (LIST + DICT)"""
    history.append({"question": question, "answer": answer})


def filter_history(keyword):
    """Example of using lambda and list comprehension"""
    return [qa for qa in history if keyword.lower() in qa["question"].lower()]


# ---------- STREAMLIT APP ----------
st.title("📚 Study Buddy – Python + AI")
st.write("Ask me anything! I'll use Gemini to answer your questions.")

# INPUT (INPUT/OUTPUT)
user_question = st.text_input("Your question:")

if st.button("Ask"):
    if user_question.strip() == "":  # CONTROL FLOW
        st.warning("Please enter a question!")
    else:
        answer = ask_gemini(user_question)  # FUNCTION CALL
        add_to_history(user_question, answer)  # SAVE TO LIST
        st.markdown(f"**Answer:** {answer}")

# SHOW CHAT HISTORY
if history:
    st.subheader("Chat History")
    for qa in history:
        st.write(f"**Q:** {qa['question']}")
        st.write(f"**A:** {qa['answer']}")

# OPTIONAL FILTER (Membership Operators + Lambda)
keyword = st.text_input("Filter history by keyword:")
if keyword:
    filtered = filter_history(keyword)
    st.write(f"Found {len(filtered)} matching questions:")
    for qa in filtered:
        st.write(f"- {qa['question']}")
