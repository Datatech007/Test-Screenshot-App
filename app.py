import streamlit as st
from playwright.sync_api import sync_playwright

st.title("🎭 Playwright Test App")

url = st.text_input("Enter URL to screenshot", "https://example.com")

if st.button("Capture Screenshot"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="screenshot.png")
        browser.close()
    st.image("screenshot.png")
