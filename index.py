import datetime
from astral import Astral
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/<string:page_name>/')
def static_page(page_name = 'index'):
    return render_template('%s.html' % page_name)

@app.route('/sunrise')
def get_sunrise():
    a = Astral()
    a.solar_depression = 'civil'
    city_candidate = request.args.get('city')
    city = a[city_candidate]
    print str(city.latitude) + ', ' + str(city.longitude)
    # return city.name
    sun = city.sun(date=datetime.datetime.now().date(), local=True)
    return jsonify(sun)

if __name__ == "__main__":
    app.run()