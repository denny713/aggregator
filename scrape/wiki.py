from datetime import datetime
import requests


def wiki_scrap(lang="en", type="title", keyword="", size=10):
    wiki_api_url = f"https://{lang}.wikipedia.org/w/api.php"
    results = []
    max_size = int(size) if size else 300
    jsdata = wiki_search(wiki_api_url, keyword, max_size)

    for page_id in jsdata:
        results.append(wiki_details(wiki_api_url, page_id, type))

    return results


def wiki_search(api_url, keyword, rs):
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": keyword,
        "srlimit": rs
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return {item['pageid']: {"title": item['title']} for item in data.get('query', {}).get('search', [])}


def wiki_details(api_url, page_id, type):
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions|info",
        "pageids": page_id,
        "rvprop": "user|timestamp|comment",
        "inprop": "url"
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    page = data.get('query', {}).get('pages', {}).get(str(page_id), {})
    revisions = page.get('revisions', [{}])[0]

    username = revisions.get('user', '')
    timestamp = revisions.get('timestamp', '')

    formatted_date = ""
    if timestamp:
        dt_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = dt_object.strftime("%Y-%m-%d")

    content = page.get('title', '') if type == 'title' else revisions.get('comment', '')

    return {
        'user': username,
        'timestamp': formatted_date,
        'rating': '',
        'content': content,
        'preview': content
    }
