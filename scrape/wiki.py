import wikipedia


def wiki_scrap(type, keyword):
    data = []
    jsdata = wiki_search(keyword)
    for obj in range(len(jsdata)):
        if type == "title":
            item = jsdata[obj]
        else:
            item = wiki_sum(jsdata[obj])
        data.append(item)

    return {"data": data}


def wiki_search(keyword, rs=20):
    return wikipedia.search(keyword, results=rs)


def wiki_sum(keyword):
    return wikipedia.summary(keyword, auto_suggest=False)
