import wikipedia


def set_language(lang="en"):
    wikipedia.set_lang(lang)


def wiki_scrap(type, keyword, size):
    results = []
    max_size = int(size) if size else 300
    jsdata = wiki_search(keyword, max_size)
    for obj in range(len(jsdata)):
        if type == "title":
            item = jsdata[obj]
        else:
            item = wiki_sum(jsdata[obj])

        results.append(item)

    return results


def wiki_search(keyword, rs):
    return wikipedia.search(keyword, results=rs)


def wiki_sum(keyword):
    return wikipedia.summary(keyword, auto_suggest=False)
