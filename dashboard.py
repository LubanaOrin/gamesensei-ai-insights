import streamlit as st
import requests

st.title("GameSensei")
deck = st.text_input("Paste your Clash Royale deck or issue:")

if st.button("Analyze"):
    result = requests.post("http://localhost:8000/analyze/", json={"deck": deck})
    st.markdown("### AI Summary")
    st.write(result.json()["summary"])
