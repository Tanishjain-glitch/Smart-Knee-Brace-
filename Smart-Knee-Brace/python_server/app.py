
from flask import Flask, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)
sensor_data = {}

def on_connect(client, userdata, flags, rc):
    client.subscribe("knee/telemetry")

def on_message(client, userdata, msg):
    global sensor_data
    sensor_data = msg.payload.decode()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

@app.route("/data")
def get_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    app.run(debug=True)
