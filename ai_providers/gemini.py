import requests
from config import GEMINI_API_KEY

def summarize_with_gemini(content):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Bạn đọc nội dung sau. Phân tích dàn ý, Tìm ra nhược điểm sau đó thêm giá trị. Và tạo ra một bài viết mới nhiều giá trị hơn nhé \n\n{content}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()
    return result["candidates"][0]["content"]["parts"][0]["text"]
