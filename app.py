from flask import Flask, render_template, request, jsonify

from scrape.acm import scrape_acm
from scrape.appstore import scrape_app_store
from scrape.bookonline import scrape_book_online
from scrape.bukalapak import scrape_bukalapak
from scrape.detik import scrape_detik
from scrape.facebook import scrape_facebook
from scrape.ieee import scrape_ieee
from scrape.instagram import scrape_instagram
from scrape.playstore import scrape_play_store
from scrape.scholar import scrape_google_scholar
from scrape.sciencedirect import scrape_science_direct
from scrape.springer import scrape_springer
from scrape.stackoverflow import scrape_stack_overflow
from scrape.tiktok import scrape_tiktok
from scrape.tokopedia import scrape_tokopedia
from scrape.twitter import scrape_twitter
from scrape.wiki import wiki_scrap
from scrape.youtube import scrape_youtube

app = Flask(__name__, static_folder='assets', template_folder='pages')
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/scrape', methods=['POST'])
def scrap():
    print("Start processing")
    req_data = request.get_json()
    print(req_data)

    module = req_data.get('module')
    typ = req_data.get('type').lower()
    search = req_data.get('search')

    match module:
        # Social media
        case "facebook":
            data = scrape_facebook(search)
        case "instagram":
            data = scrape_instagram(search)
        case "youtube":
            data = scrape_youtube(search)
        case "twitter":
            data = scrape_twitter(search)
        case "tiktok":
            data = scrape_tiktok(search)

        # QA crowdsourcing
        case "stackoverflow":
            data = scrape_stack_overflow(typ, search)

        # Application marketplace
        case "playstore":
            data = scrape_play_store(search)
        case "appstore":
            data = scrape_app_store(search)

        # Academic literature
        case "ieee":
            data = scrape_ieee(typ, search)
        case "acm":
            data = scrape_acm(typ, search)
        case "springer":
            data = scrape_springer(typ, search)
        case "scholar":
            data = scrape_google_scholar(typ, search)
        case "bookonline":
            data = scrape_book_online(typ, search)
        case "sciencedirect":
            data = scrape_science_direct(typ, search)
        case "wikipedia":
            data = wiki_scrap(typ, search)

        # Indonesia marketplace
        case "tokopedia":
            data = scrape_tokopedia(typ, search)
        case "shopee":
            data = []
        case "bukalapak":
            data = scrape_bukalapak(typ, search)

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
