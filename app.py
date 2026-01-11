from flask import Flask, request
from controllers.message_controller import MessageController
from messaging.whatsapp_handler import handle_whatsapp

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return "OK", 200

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    return handle_whatsapp()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055, debug=True)
