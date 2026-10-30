# Nasir Bhai Ka Personal Visa Bot - 100% FREE Lifetime Unlimited
from flask import Flask, request

app = Flask(__name__)

def get_reply(message):
    msg = message.lower()
    
    if "price" in msg or "rate" in msg or "kitna" in msg or "paisa" in msg or "cost" in msg:
        return "Dubai Visa 1 Year: 8.30 Lac\n2 Lac Advance, Baqi Visa Lagny k Baad.\n"
    elif "document" in msg or "docs" in msg or "kagaz" in msg or "passport" in msg:
        return "Documents:\n1- Passport\n2- CNIC Pic\n3- White Background Photo\n"
    elif "time" in msg or "kitne din" in msg or "days" in msg:
        return "InshaAllah 3-5 Working Days Me Visa Ajayega.\n"
    elif "payment" in msg or "advance" in msg or "jazzcash" in msg:
        return "2 Lac Advance. Baqi Visa Lagny K Baad.\nJazzCash / Easypaisa Available Hai.\n"
    else:
        return "Assalamu Alaikum! Visa K Liye Likhain:\nPrice, Documents, Time, Payment"

@app.route('/')
def home():
    return "Nasir Bhai Ka Personal Bot Running - FREE LIFETIME"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return request.args.get('hub.challenge', 'ok')
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
