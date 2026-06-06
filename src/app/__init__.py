from flask import Flask
from flask import request , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Data Science Service API!"

if __name__ == "__main__":
    app.run(debug=True)