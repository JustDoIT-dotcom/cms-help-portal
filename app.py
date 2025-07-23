import streamlit as st
import os
from pathlib import Path

# --- Dummy Login Credentials ---
USERS = {
    "cms": "cms@123",
    "engineer": "cms@123"
}

# --- Session State for Login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Login Form ---
if not st.session_state.logged_in:
    st.set_page_config(page_title="IR CMS Support Hub - Login", layout="centered")
    st.title("🔐 IR CMS Support Hub Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")
    st.stop()

# --- Main Portal Layout ---
st.set_page_config(page_title="IR CMS Support Hub", layout="wide")
st.title("🚆 IR CMS Support Hub – Powered by Addsoft Technologies Pvt. Ltd.")

# --- Sidebar Topics ---
st.sidebar.header("📚 Help Topics")
topics = {
    "Download CMS Image": "articles/cms_iso_info.md",
    "How to Make Bootable Pendrive": "articles/bootable_pendrive.md",
    "How to Install CMS Image": "articles/install_cms_image.md",
    "How to Check installed CMS Image Version": "articles/installed_image_version.md",
    "Test Breath Analyzer Device on Terminal": "articles/ba_terminal.md",
    "Run Photo Clearner Script": "articles/photo_cleaner.md",
    "CMS Helpline Numbers – CRIS Support": "articles/cms_helpline_number.md"

}
choice = st.sidebar.radio("Select a Topic", list(topics.keys()))

# --- Load and Show Selected Article ---
article_path = Path(topics[choice])
if article_path.exists():
    with open(article_path, "r", encoding="utf-8") as file:
        st.markdown(file.read(), unsafe_allow_html=True)
else:
    st.warning("Selected article not found.")

# --- Download Tools Section ---
st.sidebar.markdown("---")
st.sidebar.markdown("🧰 **Tools**")
download_path = "downloads/Rufus_V4.7.exe"
if os.path.exists(download_path):
    with open(download_path, "rb") as f:
        st.sidebar.download_button("Download Rufus", f, file_name="Rufus_V4.7.exe")
else:
    st.sidebar.info("Rufus tool not found.")

# --- Footer ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #333;
        text-align: center;
        padding: 10px;
        font-size: 18px;
        border-top: 1px solid #ddd;
        z-index: 100;
    }
    </style>

    <div class="footer">
        🚄 <strong>IR CMS Support Hub</strong> – Powered by <strong>Addsoft Technologies Pvt. Ltd.</strong><br>
        👨‍💻 Developed & Maintained by <strong>Mohammad Imran</strong><br>
        📧 <a href="mailto:addsoft@addsofttech.com">addsoft@addsofttech.com</a>
        📞 Contact: +91-9982134193
    </div>
    """,
    unsafe_allow_html=True
)
