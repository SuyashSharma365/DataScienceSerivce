from flask import Flask
from flask import request , jsonify
from .service.messageService import MessageService
from kafka import KafkaProducer
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()
producer = KafkaProducer(bootstrap_servers=app.config['KAFKA_BOOTSTRAP_SERVERS'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

@app.route("/v1/ds/message" , methods=["POST"])
def handleMessage():
    message = request.json.get("message")
    result = messageService.processMessage(message)
    serialized_result = result.serializer()
    producer.send(app.config['KAFKA_TOPIC'], value=serialized_result)
    return jsonify(result.model_dump()) , 200

@app.route("/" , methods=["GET"])
def home():
    return jsonify({"message": "Hello World"}), 200

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)