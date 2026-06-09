from flask import Flask
from flask import request , jsonify
from service.messageService import MessageService

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

@app.route("/v1/ds/message" , methods=["POST"])
def handleMessage():
    message = request.json.get("message")
    result = messageService.processMessage(message)
    return jsonify(result.model_dump())

@app.route("/" , methods=["GET"])
def home():
    print("Hello World")

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)