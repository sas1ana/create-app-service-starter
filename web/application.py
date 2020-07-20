from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1 style='color: red;'>Hello World!</h1>
    <p>This is a simple app</p>
    """


if __name__ == "__main__":
    app.run(port=3000)
