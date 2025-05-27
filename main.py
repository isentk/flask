from flask import Flask, request, abort
import json
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        body = request.get_data(as_text=True)
        events = json.loads(body).get("events", [])

        for event in events:
            if "source" in event and "userId" in event["source"]:
                user_id = event["source"]["userId"]
                print(f"🌟 LINE userId: {user_id}")

        return 'OK'
    except Exception as e:
        print("❌ Error:", e)
        abort(400)

@app.route('/')
def index():
    return "✅ LINE webhook is running!"
