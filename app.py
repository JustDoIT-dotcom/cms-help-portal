import streamlit as st
import os
from pathlib import Path
import base64
import csv

def NIGSServer_Check():
    IP = "122.176.115.34"
    print("The value data is:", IP)

    # ----------------------Check Ping------------------------------------
    response = os.system("ping -c 1 " + IP)
    # and then check the response...
    if response == 0:
        # messagebox.showinfo("info", "Network Active")
        print("Server Running")
        # DB_ConnChk()  # Call Database Server Running Status
    else:
        st.error("Server Connection Error")
        # messagebox.showerror("Error", "Check Internet Connection")
        exit()


# --- Login Setup ---
USERS = {
    "admin": "admin@193",
    "cms": "cms@123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

# --- Login Page ---
#NIGSServer_Check()  # Call Check NIGS Server Connection Function
st.set_page_config(page_title="IR CMS Support Hub", layout="centered")
if not st.session_state.logged_in:
    st.header("🔐 ATPL CMS Support Hub Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome {username}!")
            st.rerun()
        else:
            st.error("Invalid username or password")
    st.stop()

# --- Logout Button ---
st.sidebar.title("👤 Logged in as: " + st.session_state.username)
if st.sidebar.button("🚪 Logout"):
    logout()

# --- Admin: View Feedback Only ---
if st.session_state.username == "admin":
    st.title("📋 Feedback Dashboard")
    feedback_file = "feedback.csv"
    if os.path.exists(feedback_file):
        with open(feedback_file, "r") as f:
            reader = csv.reader(f)
            data = list(reader)
            if data:
                st.table(data)
            else:
                st.info("No feedback submitted yet.")
    else:
        st.info("Feedback file not found.")

# --- Engineer: Full CMS Help & Feedback Form ---
elif st.session_state.username == "cms":
    st.header("🚆 CMS Support Hub")

    # --- Help Topics Section ---
    st.markdown("## 📚 Help Topics")
    topics = {
        "Download CMS Image": "articles/cms_iso_info.md",
        "How to Make Bootable Pendrive": "articles/bootable_pendrive.md",
        "How to Install CMS Image": "articles/install_cms_image.md",
        "How to Check installed CMS Image Version": "articles/installed_image_version.md",
        "Test Breath Analyzer Device on Terminal": "articles/ba_terminal.md",
        "How to Update BA API": "articles/update_ba_api.md",
        "Run Photo Clearner Script": "articles/photo_cleaner.md",
        "Registration Page Not Opening During CREW Sign On/Off": "articles/crew_registration_popup_issue.md",
        "CMS Helpline Numbers – CRIS Support": "articles/cms_helpline_number.md",
        "How to Update BA Firmware (PDF)": "pdfs/ATPL BA device Firmware Help Documents(V1.1).pdf"
    }

    with st.expander("📘 Tap to Expand Help Topics"):
        choice = st.radio("Select a Help Topic:", list(topics.keys()))

    file_path = Path(topics[choice])
    if file_path.exists():
        if file_path.suffix == ".md":
            with open(file_path, "r", encoding="utf-8") as file:
                st.markdown(file.read(), unsafe_allow_html=True)
        elif file_path.suffix == ".pdf":
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                st.markdown(f"""
                    <iframe src="data:application/pdf;base64,{base64_pdf}" 
                    width="100%" height="800px" type="application/pdf"></iframe>
                """, unsafe_allow_html=True)
                st.download_button("📥 Download PDF", data=open(file_path, "rb"), file_name=file_path.name)



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
        font-size: 16px;
        border-top: 1px solid #ddd;
        z-index: 100;
    }
    @media screen and (max-width: 600px) {
        .footer {
            font-size: 13px;
            padding: 8px;
        }
    }
    </style>
    <div class="footer">
    💻 Developed by <strong>Mohammad Imran</strong><br>
    🚄 <strong>Powered by Addsoft</strong><br>
    📞 +91-9982134193
    </div>
    """,
    unsafe_allow_html=True
)
