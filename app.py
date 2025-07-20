import streamlit as st
import requests
from bs4 import BeautifulSoup
from ai_providers import gemini
from config import AI_PROVIDER

st.set_page_config(page_title="📚 ReadResumer", layout="centered")
st.title("📚 ReadResumer – Tóm tắt bài viết trong 5 giây")

# Trích nội dung từ URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = "\n".join([p.get_text() for p in paragraphs])
    return text[:5000]  # tránh vượt token

url = st.text_input("🔗 Nhập URL bài viết:")

if st.button("Tóm tắt"):
    if not url:
        st.warning("Hãy nhập URL hợp lệ.")
    else:
        with st.spinner("🔍 Đang tải bài viết..."):
            try:
                full_text = extract_text_from_url(url)

                st.subheader("📄 Nội dung gốc:")
                with st.expander("Xem nội dung trích xuất từ bài viết"):
                    st.write(full_text)

                with st.spinner("✍️ Đang tóm tắt bằng AI..."):
                    if AI_PROVIDER == "gemini":
                        summary = gemini.summarize_with_gemini(full_text)
                    else:
                        summary = "Chưa hỗ trợ AI provider này."

                st.subheader("📝 Tóm tắt 3 ý chính:")
                st.markdown(summary)

                # Nút Copy
                st.code(summary, language="markdown")
                st.button("📋 Copy vào clipboard", help="Nhấn chuột phải để sao chép thủ công")

            except Exception as e:
                st.error(f"Lỗi: {e}")
