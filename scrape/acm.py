import requests
from bs4 import BeautifulSoup


def scrape_acm(type, keyword):
    url = 'https://dl.acm.org/action/doSearch?AllField={}'.format(keyword)
    response = requests.get(url)

    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        if type == "title":
            titles = soup.find_all("h5", class_="issue-item__title")

            for title in titles:
                results.append(title.text.strip())
        elif type == "abstract":
            abstracts = soup.find_all("div", class_="issue-item__abstract")

            for abstract in abstracts:
                results.append(abstract.text.strip())
        else:
            results = []
    else:
        print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
        results = []

    return {"data": results}
