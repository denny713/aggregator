from flask import Flask, render_template, request, jsonify

from scrape.acm import scrape_acm
from scrape.detik import scrape_detik
from scrape.ieee import scrape_ieee
from scrape.sciencedirect import scrape_science_direct
from scrape.springer import scrape_springer
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
            data = []
        case "instagram":
            data = []
        case "youtube":
            data = []
        case "twitter":
            data = []
        case "tiktok":
            data = []

        # QA crowdsourcing
        case "stackoverflow":
            data = []

        # Application marketplace
        case "playstore":
            data = []
        case "appstore":
            data = []

        # Academic literature
        case "ieee":
            data = scrape_ieee(typ, search)
        case "acm":
            data = scrape_acm(typ, search)
        case "springer":
            data = scrape_springer(typ, search)
        case "scholar":
            data = []
        case "bookonline":
            data = []
        case "sciencedirect":
            data = scrape_science_direct(typ, search)
        case "wikipedia":
            data = wiki_scrap(typ, search)

        # Indonesia marketplace
        case "tokopedia":
            data = []
        case "shopee":
            data = []
        case "bukalapak":
            data = []

        # Indonesia news
        case "detik":
            data = scrape_detik(typ, search)

        # Others
        case _:
            data = []

    print("Complete processing")
    return {"data": data}


if __name__ == '__main__':
    app.run(debug=True, port=7878)
