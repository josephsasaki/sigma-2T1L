from flask import Flask, current_app, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return current_app.send_static_file("index.html")


if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(debug=True, host="0.0.0.0", port=5000)
