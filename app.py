import json
import re

import neattext.functions as nfx
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from flask import Flask, render_template, request, make_response, Response
from nltk import word_tokenize
from nltk.corpus import stopwords

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
from scrape.shopee import scrape_shopee
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
            data = scrape_shopee(typ, search)
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


@app.route('/api/preprocessing', methods=['POST'])
def preprocessing():
    req_process = request.get_json()
    req_data = json.loads(request.cookies.get('scrape-data'))
    stemmer = StemmerFactory().create_stemmer()

    # Remove username
    if 'remove_username' in req_process:
        def users(text):
            text = nfx.remove_userhandles(text)
            return text

        req_data = req_data.apply(users)

    # Remove retweet
    if 'remove_rt' in req_process:
        def rt(text):
            text = re.sub(r'^RT[\s]+', '', text)
            return text

        req_data = req_data.apply(rt)

    # Remove hashtag
    if 'remove_hashtag' in req_process:
        def hastag(text):
            text = nfx.remove_hashtags(text)
            return text

        req_data = req_data.apply(hastag)

    # Remove url
    if 'remove_url' in req_process:
        def urls(text):
            text = nfx.remove_urls(text)
            text = re.sub(r'https?:\/\/.[\r\n]', '', text)
            text = re.sub(r'http\S+', '', text)
            text = re.sub(r'\bhttp\b', '', text)
            text = re.sub(r'www.\S+', '', text)
            text = re.sub(r'\S+.com', '', text)
            text = re.sub(r'\S+.net', '', text)
            text = re.sub(r'\S+.org', '', text)
            return text

        req_data = req_data.apply(urls)

    # Remove punctuation
    if 'remove_punctuation' in req_process:
        def remove_punctuations(text):
            punct = '''.,;:-?!'"()[]/`_'''
            pattern = f'[{re.escape(punct)}]'
            text = re.sub(pattern, '', text)
            return text

        req_data = req_data.apply(remove_punctuations)

    # Remove symbol
    if 'remove_symbol' in req_process:
        def remove_symbols(text):
            punct = '''.,;:-?!'"()[]/`_'''
            pattern = rf'[^\w\s{re.escape(punct)}]'
            text = re.sub(pattern, '', text)
            return text

        req_data = req_data.apply(remove_symbols)

    # Remove number
    if 'remove_number' in req_process:
        def remove_numbers(text):
            pattern = r'\d+'
            text = re.sub(pattern, '', text)
            return text

        req_data = req_data.apply(remove_numbers)

    # Remove duplicate
    if 'remove_duplicate' in req_process:
        Y = req_data
        Y = Y.drop_duplicates(keep='first')
        req_data = Y

    # Replace slang
    if 'replace_slang' in req_process:
        def r_slang(text):

            # Membaca dataset dari file menggunakan pandas
            slang_dataset = pd.read_csv(app.root_path + '/assets/csv/slang_dataset.csv', delimiter=';',
                                        names=['slang', 'replacement'])
            slang_dict = dict(zip(slang_dataset['slang'], slang_dataset['replacement']))
            words = text.split()
            replaced_words = []

            for word in words:
                replacement = slang_dict.get(word)
                if replacement is not None:
                    replaced_words.append(replacement)
                else:
                    replaced_words.append(word)
            replaced_text = ' '.join(replaced_words)
            return replaced_text

        req_data = req_data.apply(r_slang)

    # Replace abbreviation
    if 'replace_abbreviation' in req_process:
        def r_abbre(text):

            # Membaca dataset dari file menggunakan pandas
            abbre_dataset = pd.read_csv(app.root_path + '/assets/csv/abbre_dataset.csv', delimiter=' = ',
                                        names=['abbre', 'replacement'])
            abbre_dict = dict(zip(abbre_dataset['abbre'], abbre_dataset['replacement']))
            words = text.split()
            replaced_words = []

            for word in words:
                replacement = abbre_dict.get(word)
                if replacement is not None:
                    replaced_words.append(replacement)
                else:
                    replaced_words.append(word)
            replaced_text = ' '.join(replaced_words)
            return replaced_text

        req_data = req_data.apply(r_abbre)

    # Replace elongated character
    if 'replace_elochar' in req_process:
        def replace_elongated_characters(text):
            elochart_data = pd.read_csv(app.root_path + '/assets/csv/elochar_dataset.csv', names=['elochar'])
            elochar_list = elochart_data['elochar'].tolist()
            elochar_dict = {word.lower(): None for word in elochar_list}
            words = text.split()
            processed_words = []

            for word in words:
                found = False
                for key in elochar_dict.keys():
                    if key in word.lower():
                        found = True
                        break
                if found:
                    processed_words.append(word)
                else:
                    pattern = re.compile(r'(\w)\1+')
                    replaced_word = re.sub(pattern, r'\1', word)
                    processed_words.append(replaced_word)

            processed_text = ' '.join(processed_words)
            return processed_text

        req_data = req_data.apply(replace_elongated_characters)

    # Lower case
    if 'lower_case' in req_process:
        def c_folding(text):
            text = text.lower()
            return text

        req_data = req_data.apply(c_folding)

    # Remove stopword
    if 'remove_stopword' in req_process:
        def remove_stopwords(text):
            if type(text) == list:
                stop_words = set(stopwords.words('indonesian'))
                filtered_words = [word for word in text if word.lower() not in stop_words]
                result = filtered_words
            else:
                text = text.split()
                stop_words = set(stopwords.words('indonesian'))
                filtered_words = [word for word in text if word.lower() not in stop_words]
                result = ' '.join(filtered_words)
            return result

        req_data = req_data.apply(remove_stopwords)

    # Stemming
    if 'stemming' in req_process:
        def stem_text(text):
            stemmed_text = stemmer.stem(text)
            return stemmed_text

        req_data = req_data.apply(stem_text)

    # Join case
    if 'join_case' in req_process:
        def joincase(text):
            if type(text) == list:
                text = ''.join(text)
                text = [text]
            else:
                text = text.replace(" ", "")
            return text

        req_data = req_data.apply(joincase)

    # Tokenize
    if 'tokenizing' in req_process:
        def Tokenize(text):
            tokens = word_tokenize(text)
            return tokens

        req_data = req_data.apply(Tokenize)

    res_data = []
    for i, row in enumerate(req_data):
        res_data.append(row)

    return {"data": res_data}


@app.route('/api/download', methods=['POST'])
def download():
    # data = json.loads(request.cookies.get('process-data'))
    # print(data)
    # csv_data = data.to_csv(header=True, index=False)
    #
    # return Response(
    #     csv_data,
    #     mimetype='text/csv',
    #     headers={'Content-Disposition': 'attachment;filename=data_series.csv'}
    # )

    try:
        data = json.loads(request.cookies.get('process-data'))
        df = pd.DataFrame(data)
        csv_data = df.to_csv(index=False)

        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment;filename=data_series.csv'}
        )
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)


if __name__ == '__main__':
    app.run(debug=True, port=7878)
