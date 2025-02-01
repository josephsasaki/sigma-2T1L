from flask import Flask, current_app, request

from actions import choose_random_puzzle

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return current_app.send_static_file("index.html")


@app.route("/2t1l", methods=["GET"])
def get_2t1l():
    return current_app.send_static_file("2t1l.html")


@app.route("/2t1l/puzzle", methods=["GET"])
def puzzle():
    """Returns a random selected puzzle from the database."""
    if request.method == "GET":
        random_puzzle = choose_random_puzzle()
        return random_puzzle.to_api_json(), 200
    return {"error": "Invalid request method for route."}, 400


if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(debug=True, host="0.0.0.0", port=5000)
