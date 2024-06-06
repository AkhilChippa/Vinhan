from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    message = {"message": f"Hello, {name}!"}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)