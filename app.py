import streamlit as st
import streamlit.components.v1 as components

# ===== 密碼保護 =====
def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.title("🔐 請輸入密碼")

    password = st.text_input("Password", type="password")

    if st.button("進入"):
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("密碼錯誤")

    return False


# ===== 主程式 =====
if check_password():
    with open("Temin_quiz_pro_uworld_mode_batch.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    components.html(html_content, height=900, scrolling=True)
