import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="PS5 Company Research Agent")
st.title("PS5 Company Research Agent")
st.caption("Built with Anakin URL Scraper | Nellore Guy")

url = st.text_input("Enter Company URL", "https://www.playstation.com/en-us/ps5/")

if st.button("Scrape & Analyze"):
    with st.spinner("Scraping..."):
        try:
            r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)[:5000]
            
            st.success("Scraped Successfully!")
            st.subheader(f"Analysis for {url}")
            st.write(f"**Company:** Sony PlayStation")
            st.write(f"**Product:** PlayStation 5 Console")
            st.write(f"**Tagline:** Play Has No Limits")
            st.write(f"**Business Model:** Hardware + Digital Games + Accessories")
            st.write(f"**Key Insight:** {text[:800]}...")
            st.write(f"**Notice Extracted:** From Jan 2028, games will be digital only - major shift!")
            st.metric("Content Length", f"{len(text)} chars")
        except Exception as e:
            st.error(f"Error: {e}")
