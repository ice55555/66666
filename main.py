from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7595890172:AAEjVFxa3-U7wUf_kRDklrspLjHilJmGUDU"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        data = request.json
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "你好！Bot 已启动。")
        return {"ok": True}
    return "Hello, Telegram Bot!"

def send_message(chat_id, text):
    url = f"{TELEGRAM_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)