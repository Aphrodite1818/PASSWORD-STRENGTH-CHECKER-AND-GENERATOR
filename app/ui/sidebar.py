import streamlit as st
from pathlib import Path
import sys

def sidebar():
    st.sidebar.title("CONFIGURATIONS")

    st.sidebar.checkbox("Use generated password", key="use_generated", value=False)
    st.sidebar.checkbox("Numbers", key="numbers", value=True)
    st.sidebar.checkbox("Special Characters", key="special_chars", value=True)
    st.sidebar.slider("Length", 8, 32, key="length", value=16)
    st.sidebar.checkbox("Shuffle", key="shuffle", value=True)

    return (
        st.session_state["use_generated"],
        st.session_state["numbers"],
        st.session_state["special_chars"],
        st.session_state["length"],
        st.session_state["shuffle"],
    )




