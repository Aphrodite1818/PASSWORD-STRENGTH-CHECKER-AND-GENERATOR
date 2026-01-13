import sys
from pathlib import Path
import streamlit as st
script_path = Path(__file__).resolve() 
parent_path = script_path.parents[1]  
sys.path.append(str(parent_path))


from core.p_generator import gen_password
from core.entropy_checker import calculate_entropy
from core.P_Validator import Password_Validator





st.set_page_config(page_title="Password Strength Checker", layout="centered",
                   page_icon=":lock:")



st.title("🔐 Password Strength Checker",text_alignment="center")
st.write("use this tool to check how secure your password is, you can also generate a strong one automatically.")


if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""



