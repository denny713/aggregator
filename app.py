from flask import Flask, render_template, request, jsonify

from scrape.acm import scrape_acm
from scrape.wiki import wiki_scrap

app = Flask(__name__, static_folder='assets', template_folder='pages')
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/scrape', methods=['POST'])
def scrap():
    req_data = request.get_json()
    print(req_data)

    module = req_data.get('module')
    typ = req_data.get('type').lower()
    search = req_data.get('search')

    match module:
        case "wikipedia":
            data = wiki_scrap(typ, search)
        case "acm":
            data = scrape_acm(typ, search)
        case _:
            data = {"data": []}

    print("Complete processing")
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=7878)
