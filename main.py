from flask import Flask, json, jsonify, request, render_template
from test import chatbot_response
import ast
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
