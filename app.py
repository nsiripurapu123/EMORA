from flask import Flask, request, jsonify
from main import chatbot

app = Flask(__name__)

@app.route("/")
def home():
    return "Emora chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    response, _, _, _ = chatbot(user_input)

    return jsonify({
        "reply": response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)