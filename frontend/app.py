import sys
import os
import asyncio
import streamlit as st
import nest_asyncio

nest_asyncio.apply()


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from client.agent import run_agent

st.set_page_config(page_title="MCP Agentic AI", layout="wide")
st.title("🤖 MCP-Based Agentic AI Assistant")

question = st.text_area("Enter your question", height=120)

if st.button("Run Agent"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = asyncio.get_event_loop().run_until_complete(
                run_agent(question)
            )
        st.success("Done ")
        st.write(answer)
