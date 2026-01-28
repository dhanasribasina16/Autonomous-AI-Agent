import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Autonomous AI Agent")

st.title("🤖 Autonomous AI Agent")
st.write("Enter a task and let the AI agent handle it.")

user_input = st.text_input("Your task:")

if st.button("Run Agent"):
    if user_input:
        with st.spinner("Thinking..."):
            result = run_agent(user_input)
        st.success("Result:")
        st.write(result)
