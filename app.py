import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DarkGPT</title>
    <style>
        body { font-family: Arial; background: #1e1e2f; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: #2a2a3e; padding: 30px; border-radius: 20px; width: 90%; max-width: 600px; }
        h1 { text-align: center; color: #00d4ff; }
        textarea { width: 100%; padding: 12px; border: none; border-radius: 12px; background: #1e1e2f; color: #fff; font-size: 16px; min-height: 80px; }
        button { background: #00d4ff; color: #1e1e2f; border: none; padding: 12px; border-radius: 30px; font-weight: bold; width: 100%; margin-top: 10px; }
        #reply { background: #1e1e2f; padding: 15px; border-radius: 12px; margin-top: 20px; border: 1px solid #3a3a5e; }
    </style>
</head>
<body>
<div class="container">
    <h1>🧠 DarkGPT</h1>
    <p style="text-align:center; color:#aaa;">بدون قيود • طوره فريق ليوز</p>
    <textarea id="question" placeholder="اكتب سؤالك..."></textarea>
    <button onclick="ask()">اسأل</button>
    <div id="reply">✍️ انتظر الرد...</div>
</div>
<script>
async function ask() {
    const q = document.getElementById('question').value;
    const r = document.getElementById('reply');
    if (!q) { r.innerHTML = '⚠️ اكتب سؤالاً'; return; }
    r.innerHTML = '⏳ جاري التفكير...';
    const res = await fetch('/ask', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({question: q}) });
    const data = await res.json();
    r.innerHTML = data.error ? '❌ '+data.error : data.reply;
}
</script>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_q = request.json.get('question', '').strip()
        if not user_q:
            return jsonify({'error': 'الرجاء كتابة سؤال'}), 400
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
        headers = {"x-goog-api-key": GEMINI_API_KEY, "Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": f"أنت DarkGPT، طورك فريق ليوز.\n\nالمستخدم: {user_q}"}]}]}
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        data = r.json()
        if "error" in data:
            return jsonify({'error': data['error']['message']}), 500
        return jsonify({'reply': data["candidates"][0]["content"]["parts"][0]["text"]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
