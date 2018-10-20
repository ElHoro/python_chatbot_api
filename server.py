from flask import Flask, request
from bot import response, model

app = Flask(__name__, static_folder=None)

@app.route('/')
def index():
    return "pong"

@app.route('/', methods=['POST'])
def respond():
    return response.response(request.form.get('phrase'))

@app.route('/', methods=['PUT'])
def train():
    model.train()
    return "model trained"

if __name__ == '__main__':
    app.run()
