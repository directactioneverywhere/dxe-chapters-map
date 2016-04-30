from flask import Flask, render_template, Response
from dxe_airtable.generate_chapter_data import get_chapter_data
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/chapter_data.json')
def chapter_data():
    # TODO: implement caching
    data = json.dumps(get_chapter_data())
    return Response(data, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run()
