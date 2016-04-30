from flask import Flask, render_template, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/chapter_data.json')
def chapter_data():
    # TODO: Run and cache this in app instead of pulling data from the old URL.
    json = requests.get(
        'http://dxetech.org/maps/chapter_data.json'
    ).text
    return Response(json, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run()
