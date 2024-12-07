import requests
from bs4 import BeautifulSoup


def scrape_acm(type, keyword, size):
    base_url = 'https://dl.acm.org'
    url = '{}/action/doSearch?AllField={}'.format(base_url, keyword)
    response = requests.get(url)
    max_size = int(size) if size else 300

    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        if type == "title":
            titles = soup.find_all("h5", class_="issue-item__title")

            for title in titles:
                results.append(title.text.strip())

                if len(results) == max_size:
                    break
        elif type == "abstract":
            abstracts = soup.find_all("h5", class_="issue-item__title")

            for abstract in abstracts:
                link = abstract.find('a', href=True)['href']
                detail_uri = base_url + link
                detail_response = requests.get(detail_uri)
                detail_soup = BeautifulSoup(detail_response.content, "html.parser")
                abstract_text = detail_soup.find("div", attrs={"role": "paragraph"}).text
                results.append(abstract_text)

                if len(results) == max_size:
                    break
        else:
            results = []
    else:
        print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
        results = []

    return results
