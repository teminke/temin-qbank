import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Temin Qbank", layout="wide")

st.title("Temin 題庫")

html_path = Path("Temin_quiz_pro_uworld_mode_batch.html")
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1100, scrolling=True)