# 🔍 Check Installed CMS Image Version

Follow these steps to check the currently installed CMS image version on your Thin-Client:

---

### 🖥️ Step-by-step Instructions:

1. **Start CMS in Thin-Client Mode**
   - Click on the **"Thin-Client"** icon (🖥️ PC icon) available on the **bottom panel** of the desktop.

2. **Open Terminal**
   - Right-click on the desktop and choose **"Open Terminal"**.

3. **Run Version Command**
   - Type the following command and press `Enter`:
     ```bash
     sudo setup
     ```
     - If prompted for a password, enter:  
     **`111`**
4. ✅ Choose Option number ***1***

   - ✅ The output will display the **CMS image version**, build date, and other system info.

---

### 💡 Tip:
If `osinfo` does not work, try:
```bash
lsb_release -a
