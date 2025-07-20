import streamlit as st
from newspaper import Article
from ai_providers import gemini
from config import AI_PROVIDER

st.set_page_config(page_title="📚 ReadResumer", layout="centered")
st.title("📚 ReadResumer – Tóm tắt bài viết trong 5 giây")

url = st.text_input("🔗 Nhập URL bài viết:")

if st.button("Tóm tắt"):
    if not url:
        st.warning("Hãy nhập URL hợp lệ.")
    else:
        with st.spinner("🔍 Đang tải và xử lý bài viết..."):
            try:
                article = Article(url)
                article.download()
                article.parse()
                content = article.text

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
