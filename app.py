import streamlit as st
import requests
from io import BytesIO

st.title("Screenshot Automation")

# Button to trigger screenshot generation
if st.button("Generate Screenshot"):
    st.write("Processing... Please wait.")
    
    # Call the Flask backend endpoint
    response = requests.get("http://<FLASK_BACKEND_URL>/screenshot")  # Replace with actual URL

    if response.status_code == 200:
        st.write("Screenshot generated successfully!")
        st.image(BytesIO(response.content), caption="Generated Screenshot")
    else:
        st.write("Error: Could not generate screenshot.")
