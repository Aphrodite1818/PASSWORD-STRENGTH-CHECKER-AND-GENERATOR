import sys
from pathlib import Path
import streamlit as st

script_path = Path(__file__).resolve()
parent_path = script_path.parents[1]
sys.path.append(str(parent_path))

from core.p_generator import gen_password
from core.entropy_checker import calculate_entropy
from core.P_Validator import Password_Validator




from ui.sidebar import sidebar
from ui.form import form

st.set_page_config(
    page_title="Password Strength Checker",
    layout="centered",
    page_icon=":lock:",
    initial_sidebar_state="expanded",
)

st.title("🔐", anchor=False)
st.title("Password Strength Checker", anchor=False)






if "password" not in st.session_state:
    st.session_state["password"] = ""

use_generated, numbers, special_chars, length, shuffle = sidebar()

if use_generated and st.session_state["password"] == "":
    st.session_state["password"] = gen_password(
        LENGTH=length,
        NUMBERS=numbers,
        SPECIAL_CHARACTERS=special_chars,
        SHUFFLE=shuffle,
    )

form = form()