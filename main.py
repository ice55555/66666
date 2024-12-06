from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Telegram Bot is running!"

TOKEN = "7595890172:AAEjVFxa3-U7wUf_kRDklrspLjHilJmGUDU"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

# 这里的路由路径是以 TOKEN 为路径
@app.route(f'/{TOKEN}', methods=["POST"])  
def webhook():
    if request.method == "POST":
        data = request.json
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "你好！Bot 已启动。")
        return {"ok": True}
    return "Hello, Telegram Bot!"  # 默认返回的消息

def send_message(chat_id, text):
    url = f"{TELEGRAM_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 确保服务可以外部访问
