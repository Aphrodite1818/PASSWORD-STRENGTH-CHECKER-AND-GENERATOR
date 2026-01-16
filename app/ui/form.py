import streamlit as st


def form():
    with st.form(key='my_form'):
        st.subheader("Password Form")
        
        st.form_submit_button("🔁 Regenerate Password")

