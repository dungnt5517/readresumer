import requests
from config import GEMINI_API_KEY

def summarize_with_gemini(content):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Tóm tắt bài viết sau thành 3 ý chính ngắn gọn, dễ hiểu:\n\n{content}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=data)
    response.raise_for_status()
    candidates = response.json().get("candidates", [])
    if not candidates:
        return "Không có kết quả từ Gemini."
    return candidates[0]["content"]["parts"][0]["text"]
