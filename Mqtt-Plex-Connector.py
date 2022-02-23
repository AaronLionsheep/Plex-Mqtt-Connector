from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json
import os
import paho.mqtt.publish as publish

app = Flask(__name__)
api = Api(app)

host = os.environ.get('MQTT_BROKER_URI')
topic = 'plex/'

@app.route('/', methods=['POST'])
def webhook():
    data = json.loads(request.form['payload'])
    publish.single(topic + data['Player']['uuid'], data, hostname=host)
    
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
