import streamlit as st
import requests
from bs4 import BeautifulSoup
from ai_providers import gemini
from config import AI_PROVIDER

st.set_page_config(page_title="📚 ReadResumer", layout="centered")
st.title("📚 ReadResumer – Tóm tắt bài viết trong 5 giây")

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lấy nội dung từ các thẻ <p>
    paragraphs = soup.find_all('p')
    text = "\n".join([p.get_text() for p in paragraphs])
    return text[:5000]  # tránh gửi quá nhiều token cho API

url = st.text_input("🔗 Nhập URL bài viết:")

if st.button("Tóm tắt"):
    if not url:
        st.warning("Hãy nhập URL hợp lệ.")
    else:
        with st.spinner("🔍 Đang tải và xử lý bài viết..."):
            try:
                content = extract_text_from_url(url)

                if AI_PROVIDER == "gemini":
                    summary = gemini.summarize_with_gemini(content)
                else:
                    summary = "Chưa hỗ trợ AI provider này."

                st.subheader("📝 Tóm tắt 3 ý chính:")
                for line in summary.split("\n"):
                    if line.strip():
                        st.markdown(f"- {line.strip()}")

            except Exception as e:
                st.error(f"Lỗi: {e}")
