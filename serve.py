from flask import Flask, request, jsonify
from autocorrect import Autocorrect

# Load corpus and initialize model
with open("big.txt", "r", encoding="utf-8") as f:
    corpus = f.read()
model = Autocorrect(corpus)

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"})

@app.route("/invocations", methods=["POST"])
def invoke():
    data = request.get_json(force=True)
    word = data.get("word", "")
    suggestion = model.correction(word) if word else ""
    return jsonify({"input": word, "suggestion": suggestion})
