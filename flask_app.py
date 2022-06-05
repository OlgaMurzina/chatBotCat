# Запускающий файл - технология CallBack - уже работает в облаке PythonAnyWhere.com

from flask import Flask, request, json

import messageHandler
import settings

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return settings.confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object']['message'], settings.token)
        return 'ok'
