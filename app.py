import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Screenshots_Automation", layout="centered")

st.title("📸 Screenshots_Automation")
st.write("This tool will automatically capture and save Looker Studio screenshots to your folders.")

# Check if google_login.json exists
if not os.path.exists("google_login.json"):
    st.warning("⚠️ Missing 'google_login.json'. Please make sure it's in the same folder before running the automation.")

if st.button("▶️ Run Screenshot Automation"):
    with st.spinner("Running automation... This may take a couple of minutes."):
        try:
            # Run the script in a subprocess (you can replace this with importing and calling a function later)
            result = subprocess.run(["python", "screenshot_automation.py"], capture_output=True, text=True)

            if result.returncode == 0:
                st.success("✅ Screenshots captured and saved successfully!")
            else:
                st.error("❌ Automation failed. See details below:")
                st.code(result.stderr)
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
