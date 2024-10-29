from flask import Flask, render_template, request, jsonify

from scrape.acm import scrape_acm
from scrape.detik import scrape_detik
from scrape.ieee import scrape_ieee
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
        # Social media
        case "facebook":
            data = {"data": []}
        case "instagram":
            data = {"data": []}
        case "youtube":
            data = {"data": []}
        case "twitter":
            data = {"data": []}
        case "tiktok":
            data = {"data": []}

        # QA crowdsourcing
        case "stackoverflow":
            data = {"data": []}

        # Application marketplace
        case "playstore":
            data = {"data": []}
        case "appstore":
            data = {"data": []}

        # Academic literature
        case "ieee":
            data = scrape_ieee(typ, search)
        case "acm":
            data = scrape_acm(typ, search)
        case "springer":
            data = {"data": []}
        case "scholar":
            data = {"data": []}
        case "bookonline":
            data = {"data": []}
        case "sciencedirect":
            data = {"data": []}
        case "wikipedia":
            data = wiki_scrap(typ, search)

        # Indonesia marketplace
        case "tokopedia":
            data = {"data": []}
        case "shopee":
            data = {"data": []}
        case "bukalapak":
            data = {"data": []}

        # Indonesia news
        case "detik":
            data = scrape_detik(typ, search)

        # Others
        case _:
            data = {"data": []}

    print("Complete processing")
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=7878)
