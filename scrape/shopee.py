import requests
from bs4 import BeautifulSoup


def scrape_shopee(type, keyword):
    results = []
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    if type == "toko":
        # keyword = 'https://shopee.co.id/buyer/1131682506/rating?shop_id=1131389131'
        toko_response = requests.request("GET", keyword, headers=header)
        soup_toko = BeautifulSoup(toko_response.content, "html.parser")
        print(soup_toko.prettify())
        toko_content = soup_toko.find_all('div', class_='shopee-product-rating__main')
        for content in toko_content:
            comment = content.find(style="position: relative; box-sizing: border-box;").text.strip()
            print(comment)
            results.append(comment)

    elif type == "produk":
        results = []
    else:
        results = []

    return results
