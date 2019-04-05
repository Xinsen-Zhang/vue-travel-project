import flask
from flask import jsonify, request
from home import get_home_data
from city import get_city

app = flask.Flask(__name__)

@app.route('/api/home')
def home_ajax():
    if request.method == 'GET':
        city = request.args.get("city")
        if city:
            pass
        else:
            city= '北京'
        return jsonify(get_home_data(city))
@app.route('/api/city')
def city_ajax():
    if request.method == 'GET':
        return jsonify(get_city())

if __name__ == '__main__':
    app.run(host='localhost')