import requests
import wikipedia


def set_language(lang="en"):
    global WIKI_API_URL
    WIKI_API_URL = f"https://{lang}.wikipedia.org/w/api.php"


def wiki_scrap(type, keyword, size):
    set_language()
    results = []
    max_size = int(size) if size else 300
    jsdata = wiki_search(keyword, max_size)

    for page_id in jsdata:
        results.append(wiki_details(page_id, type))

    return results


def wiki_search(keyword, rs):
    # params = {
    #     "action": "query",
    #     "format": "json",
    #     "list": "search",
    #     "srsearch": keyword,
    #     "srlimit": rs
    # }
    # response = requests.get(WIKI_API_URL, params=params)
    # data = response.json()
    # return {item['pageid']: {"title": item['title']} for item in data.get('query', {}).get('search', [])}
    return wikipedia.search(keyword, results=rs)


def wiki_details(page_id, type):
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions|info",
        "pageids": page_id,
        "rvprop": "user|timestamp|comment",
        "inprop": "url"
    }
    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()

    page = data.get('query', {}).get('pages', {}).get(str(page_id), {})
    revisions = page.get('revisions', [{}])[0]

    username = revisions.get('user', '')
    timestamp = revisions.get('timestamp', '')

    if type == 'title':
        content = page.get('title', '')
    else:
        content = revisions.get('comment', '')

    return {
        'user': username,
        'timestamp': timestamp,
        'rating': '',
        'content': content,
        'preview': content
    }

# import wikipedia
#
#
# def set_language(lang="en"):
#     wikipedia.set_lang(lang)
#
#
# def wiki_scrap(type, keyword, size):
#     results = []
#     max_size = int(size) if size else 300
#     jsdata = wiki_search(keyword, max_size)
#     for obj in range(len(jsdata)):
#         if type == "title":
#             item = jsdata[obj]
#         else:
#             item = wiki_sum(jsdata[obj])
#
#         results.append(item)
#
#     return results
#
#
# def wiki_search(keyword, rs):
#     return wikipedia.search(keyword, results=rs)
#
#
# def wiki_sum(keyword):
#     return wikipedia.summary(keyword, auto_suggest=False)
