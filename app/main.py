from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Bad DevSecOps API running"}), 200


@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()

    if not data or "a" not in data:
        return jsonify({"error": "Invalid input"}), 400

    a = data["a"]
    b = data["b"] 

    return jsonify({"result": a + b}), 200


if __name__ == "__main__":
    app.run(debug=True)
