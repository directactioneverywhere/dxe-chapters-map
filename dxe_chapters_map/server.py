from flask import Flask, render_template, Response
from werkzeug.contrib.cache import SimpleCache
from dxe_airtable.generate_chapter_data import get_chapter_data
import json

app = Flask(__name__)
cache = SimpleCache()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chapter_data.json')
def chapter_data():
    data = cache.get('chapter-data')
    if data is None:
        data = json.dumps(get_chapter_data())
        # Cache for 20 minutes
        cache.set('chapter-data', data, timeout=20*60)
    return Response(data, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()
