from flask import Flask, send_from_directory
import random

app = Flask(__name__, static_folder='../client/public')

@app.route("/")
def base():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def home(path):
        return send_from_directory(app.static_folder, path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True)