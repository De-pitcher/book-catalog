# book_service/app.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/books")
def books():
    return jsonify(["1984", "Dune", "Harry Potter"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)