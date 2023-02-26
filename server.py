from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def base():
    return send_from_directory("client/public", "index.html")

@app.route("/<path:path>")
def home(path):
        return send_from_directory("client/public", path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True)