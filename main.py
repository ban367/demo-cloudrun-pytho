import os
from flask import Flask, jsonify

app = Flask(__name__)


def response_message(code, message='OK'):
    return jsonify({'code': code, 'message': message})


@app.route('/', methods=['GET'])
def hello():
    return response_message(200)


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8000))
    )
