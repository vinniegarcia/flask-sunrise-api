import datetime
from astral import Astral
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sunrise')
def get_sunrise():
    a = Astral()
    a.solar_depression = 'civil'
    city = a['San Francisco']
    print str(city.latitude) + ', ' + str(city.longitude)
    # return city.name
    sun = city.sun(date=datetime.datetime.now().date(), local=True)
    return jsonify(sun)
