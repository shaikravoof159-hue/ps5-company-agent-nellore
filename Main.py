import streamlit as st
import requests
from bs4 import BeautifulSoup
st.set_page_config(page_title="PS5 Agent Nellore")
st.title("PS5 Company Research Agent")
st.caption("Built with Anakin URL Scraper | Nellore Guy")
url = st.text_input("Enter Company URL", "https://www.playstation.com/en-us/ps5/")
if st.button("Scrape & Analyze"):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()[:3000]
        st.success("Scraped Successfully")
        st.write(text[:1500])
        st.info("PS5 Strategy: Partner for accessories in Nellore")
    except Exception as e:
        st.error(str(e))
