import flask
from flask import jsonify, request
from home import get_home_data

app = flask.Flask(__name__)

@app.route('/api/home')
def home_ajax():
    if request.method == 'GET':
        return jsonify(get_home_data())


if __name__ == '__main__':
    app.run(host='localhost')