import urllib
from datetime import datetime

import requests

from scrape.data_sp import get_products_code, get_shop_id, get_user_id, get_product_reviews


def scrape_shopee(type, keyword, size):
    max_size = int(size) if size else 100

    results = []
    if type == "toko":
        query = urllib.parse.quote_plus(keyword)
        url = "https://shopee.co.id/api/v4/shop/get_shop_base"
        params_toko = {
            "entry_point": "ShopBySearch",
            "need_cancel_rate": "true",
            "request_source": "shop_home_page",
            "username": query,
            "version": "2"
        }

        headers_toko = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "af-ac-enc-dat": "95fa3a36402c0725",
            "af-ac-enc-sz-token": "8eNzXUefYnmDp1b/zztoYw==|C1kuACa6aFlZDpJM9dRd/3W7Uto69vkO6o9ZAlJB802S9+jhB4SulLsLviSkM98KT0M478/5Uj5/kbPn0to=|3l2i/Y9ZFRXhbx9V|08|3",
            "content-type": "application/json"
        }

        cookies_toko = {
            "SPC_F": "WFUzheCtWTSFxqjks1jtzLK2OILH1eq7",
            "REC_T_ID": "65bc9746-8775-11ef-8fe2-02a857dbf833",
            "SPC_CLIENTID": "WFUzheCtWTSFxqjkbjzhebonzkjnwwdp",
            "REC7iLP4Q": "93755e7c-fee3-4895-9ba6-2b2301b77814",
            "__LOCALE__null": "ID",
            "csrftoken": "IqNqb7aO173Hl6Thl7GFoCFNLBxKQqfc",
            "_QPWSDCXHZQA": "e269860c-3337-4fbd-f14b-87289f458bf5",
            "_sapid": "8ff47aa8997c72cf8aa9b6aa9c63b44acc04393235ff9f6b9396e6cf",
            "SPC_SEC_SI": "v1-ODZneFVCOHJZUm1jYUNJMNAC9RGj4FWXlZg30w2sjfu3H5t7LvzxRPCBgV0Np2VKDExVX1vuifIszBSQDunXYBj6A7i6fX/MAP/Sg/tyjhQ=",
            "SPC_SI": "+O2+ZwAAAAB5UGlnOXN6efjriAAAAAAASUhMbXlRZGk="
        }

        response_toko = requests.get(url, params=params_toko, headers=headers_toko, cookies=cookies_toko).json()

        try:
            shop_id = response_toko['data']['shopid']
        except:
            shop_id = get_shop_id()

        print(shop_id)

        try:
            user_id = response_toko['data']['userid']
        except:
            user_id = get_user_id()

        print(user_id)

        url_detail_toko = 'https://shopee.co.id/api/v4/seller_operation/get_shop_ratings_new?limit={}&offset=0&replied=false&shopid={}&userid={}'.format(
            max_size, shop_id, user_id)
        response_toko_detail = requests.get(url_detail_toko).json()
        reviews = response_toko_detail['data']['items']
        for review in reviews:
            comment = review['comment']
            timestamp = review['ctime']
            formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

            results.append({
                'user': review['author_username'],
                'timestamp': formatted_date,
                'rating': review['rating_star'],
                'content': comment,
                'preview': comment
            })

    elif type == "produk":
        query = urllib.parse.quote(keyword)
        url = "https://shopee.co.id/api/v4/search/search_items"
        url_referrer = 'https://shopee.co.id/search?keyword={}'.format(query)
        params = {
            "by": "relevancy",
            "extra_params": "%7B%22global_search_session_id%22%3A%22gs-df28216b-20e0-412e-8c90-5f061118ef81%22%2C%22search_session_id%22%3A%22ss-42dba405-b7bd-44f6-84c7-6a7009ef2f5b%22%7D",
            "keyword": keyword,
            "limit": max_size,
            "newest": "0",
            "order": "desc",
            "page_type": "search",
            "scenario": "PAGE_GLOBAL_SEARCH",
            "source": "SRP",
            "version": "2",
            "view_session_id": "3cc09182-0a19-49bc-b86b-646d7f4cd99e"
        }

        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "af-ac-enc-dat": "3b5d22463ffb7eda",
            "af-ac-enc-sz-token": "9ksAHupK+wlgr0nX8Yj8sw==|JlkuACa6aFlZDpJM9dRd/3W7Uto69vkO6o9ZAi56ru+S9+jhB4SulLsLviSkM98KT0M478/5Uj5/kbPn0to=|3l2i/Y9ZFRXhbx9V|08|3",
            "content-type": "application/json",
            "d-nonptcha-sync": "AAAGzjAcInMAAAEAAAaK5SgvdVHbicID/wIiAAAFMA==",
            "priority": "u=1, i",
            "referer": url_referrer,
            "sec-ch-ua": '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133")',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "sz-token": "9ksAHupK+wlgr0nX8Yj8sw==|JlkuACa6aFlZDpJM9dRd/3W7Uto69vkO6o9ZAi56ru+S9+jhB4SulLsLviSkM98KT0M478/5Uj5/kbPn0to=|3l2i/Y9ZFRXhbx9V|08|3",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "x-api-source": "pc",
            "x-csrftoken": "Zg12tIhLx60Ao1eKhs3OqNSjA04nUri8",
            "x-requested-with": "XMLHttpRequest",
            "x-sap-ri": "6f20e1671655fbab8473503a0501dffb5b3784106550ab0c26ec",
            "x-sap-sec": "lrnGnTv+OGRqE8W7etB7e8s7atBTetW7VLMmeWB76t+ieXC7AGMPe9E7sG+ae1K7Rh+geuB74GMSeWn7NLMke9B77tBfe8W7shMceUs7ctMoe9f7UhBqetf7+tMzeWD7bt+Ce9v7ptMqeqW72tByeVI7utBGeq/7vtNKenB7ZtBkeXI74LM7eqB7QhMievs7ThBLeWO7vhB7etB7eXbHuxaSrFrVqi+BycC7KSLvj00QdkB7etMoeLB7etB7y8joDSx7scAgdVW7cmc9RdhkehB7VE7ovGB7Uqv7eVpGk1C72ZW3etB7e8B82f4f1LO0etMoYhBX4DDr+GBiMeC720v49HoAotB7e4nBTAreetB7tCO3etB7eUxxbt/7etB7eqrGWTfBNlJxVE79coO9etB7eUXrZ5f/etB7tlHletbx/ihT8LF1eLB7etB7mvdw35/7etMF9tK7etB764UdevbyEtB7enx8LQqDeGB78JTOUpo7TM15Tn43ECRY6HlWom9BAwaKZQLC3CQQ0F5ji6AbhgEkhjO66HI31QE0lJDs/CuSXFWL95egZOV0r3vJ6qPNfaaQXbZvimi3qmqsiTAFC3QyBX9UhVzKeh8UYSx3M2yZbO8x17LlpZCgkcSmmcZL5+VKm2GzcNhGrew9HVEzA5Ao1q2Wc9BEnZXjcVTjUUQK7RtSp8xhnYLCji5TtoPH3WB5Hz+8ycDHz7D/t0l6VxMym0g+jqy5oiIbKnn0WYGYRxcC1TnUD8al8CSZHKbBHQH/EVK72Yj0cdZAJAUodXD7q2C/2wNOx+EBqBDg2lPMml3gXukJoxDww1dcD1Tefvw4SvD5nNJhBcCIw3FhNaQSOzFkcf/wlBHvq4aevXpEcvp9KTWsWi488DtzzzuN/JgNtunq5saeQA79RB360vHzSQlWvD8cPqVAizkkJM4YElTqL2uhNzgebW/2DGbPPSLkhNNZS0xfzrnXnsD+TwxPwApCfEH+79MxlGrCyejr7PHsg8rIJyu9PFbEbmm/xier4INbLEHN1rIL/U4mFmGvoofhk0heNLvXGQaIBFpQyoZZKGB7whB7eXcfUuSqhRBSusF18c/KdFHQV24PWxxepQ2668pCPkEiKJfo9Tws40SUiM/PMDR3wtNwQIa/IbrnpkB3lLZeRANawFW18yrono3mhNF0Tz80IFWT7NkFm1vAuo3W3VlJoQfq0uSK1lz8A4nHbSqaP4JbRHzXpif5Xu2SkY5iT32e0UHOJaObxpzygWT8RwZmP+t8gSII+20ZQKXCNHk6jtMB3ZOYrEz2nOfqAFRm4Dpi93yJvXo2WUFGXRKMObVpwN1ppZYBNvKtrCM8Qy0mvpBb3mxGdpqEbDDSetB0etB7bDub/Lf7et+I0e2dTRvgjLK7etBx6LB7etB7etB7et+3etB743UN2ehQBSPILbeh4/c+KvJu6EJ2Q0DX+UGKR7J636QncZhi2eP16eDAQvLY403hO/Jqd0sABHZMOHvA2ecl/HcvBwZerwZlRUKqL7Ji713+BHmeR3DArUZoPUDqO0fgOxJlOwUmcEMfP1PgkaWUdqLz4/lA2ehE2VgxNqms+qBT+q/7ItB7eUfwuierXr1PKu0elhuviOt7BMAx0R1yUnWZZ+/M9T9P314sWLB7etBdetB7PogCrqIVQbI7etB7HtB7e1lsF8BWYcYj",
            "x-shopee-language": "id",
            "x-sz-sdk-version": "1.12.17",
            "Cookie": "SPC_F=WFUzheCtWTSFxqjks1jtzLK2OILH1eq7; REC_T_ID=65bc9746-8775-11ef-8fe2-02a857dbf833; SPC_CLIENTID=WFUzheCtWTSFxqjkbjzhebonzkjnwwdp; _QPWSDCXHZQA=e269860c-3337-4fbd-f14b-87289f458bf5; REC7iLP4Q=93755e7c-fee3-4895-9ba6-2b2301b77814; SPC_ST=.YnRvMlppOTlMTWdYa3NpYt7MHo0O+rVZ7I6wFEHybgvwQIqvfyjfFTuE9pcq/rheMziMPxX1/FU0h42hYXNEGkzva2cQBsXD3zox31L2Zv4nCkYHL1MQA/ZaXUvhHMoQaIBs6SdygIJfk9tfO4XPiaVFCQd+Dc4royLk9tHmfGsnzhKSdaZB0Y2tErjlBynqydykb3MBLh65PDm5+S9IIxFNwtQ7QvwYL38I0xxDbM5mqJ9nVoKaYopHTja+ZVw9; SPC_U=259698873; SPC_R_T_ID=x+R9PQxoXuSoPOiIVlyOWLemUbwPG5PU+ZwFIO59he4xI9ZTmWjayiPXciVK+pZbwFOmo39kCCk9m4oxPTFOc7EA/f8lhF/hyd96xSlHqPHBD48dLOKM1AvJAsnrv8GtHW5c0OJnAiGclKOiR6CG2OXuoLz/NIeT50BDo9e0gk4=; SPC_R_T_IV=VTJzTGdrV01oMU1iYUNTeg==; SPC_T_ID=x+R9PQxoXuSoPOiIVlyOWLemUbwPG5PU+ZwFIO59he4xI9ZTmWjayiPXciVK+pZbwFOmo39kCCk9m4oxPTFOc7EA/f8lhF/hyd96xSlHqPHBD48dLOKM1AvJAsnrv8GtHW5c0OJnAiGclKOiR6CG2OXuoLz/NIeT50BDo9e0gk4=; SPC_T_IV=VTJzTGdrV01oMU1iYUNTeg==; __LOCALE__null=ID; csrftoken=Zg12tIhLx60Ao1eKhs3OqNSjA04nUri8; _sapid=8ff47aa8997c72cf8aa9b6aa9c63b44acc04393235ff9f6b9396e6cf; SPC_SEC_SI=v1-Q2dmR1FEUFN1S1lXSUZybKNlPxbwxAF+cgaOWO98aGojBO1GmX9H7NFjO6dRHV+2G+8LkvdXkdMCPiY+wgueE3JsBuDwKGr3sehbKw/dc80=; SPC_SI=wRnIZwAAAABTcWQ2WmlwQVT82wAAAAAAbTI0c1c1bWw=; SPC_IA=1; SPC_CDS_CHAT=d9e32805-53b9-4f32-876b-486af2292538; AC_CERT_D=U2FsdGVkX19wTUH/ZmpUo5jIusgFh6d/AqMprFjS1LGnGeohbHs2guTnPF+tErTsLKVAJFsX1erEWzyi0lrbEAIbuHn7d+fqSfra0mDAClgeFse1PPF3vZXXgKymtkZ7cIcoFaJ3vPjOsXzNZqpbIMQsw+ruUS/7KDsj4UQyZOF66pt20VjVPmShjSa6FSl1RS7SCeLZ8PBweupczexQ5uiMqr6x3Rz06Fh7V4JCNlzCh6i4h35Cz/JKaEmZMTp+PhkooARcvJkR3LDRfKMhFpPQGhRwrfRsAnechkYaek+DZ+ijbxUf4IpHU3m9l/vk7ZcbYhfV6AriDKBkRG0hC8/mZ/pDoMZuFLPLlib0kFC7njQJhGrTwJImuUBUbjaPziUaOjeeJkl0IXMPQdMVHQbdi5genUGVZz3b0s/99FoKQHLjXRpuQbhpcScFawd5vIn2znHMDusiw4mp9NlNka8SANTNWRxylY7zHPUFQMQCccCowBP1eMKyh5ZkRKem2HcLdyJGdgTmTbdJ2pP85DRWqYR0+gtH5IiSIO5ijGCtzTBsaOy2qmXXWY1Fdj0ITQ8MoVsHMUG7u1AJfzhRGxDm0fcs5qBAvfVrLTOL5WmnXSvRPLJ6hJ7KbkxCV4bz64y9XxnR/lmSt716rdFHNr/gp8w+HaOHpMxQJ94GYuXhJsZVzssSwGkLOXZAMhoI9Se0duSWmne+tXfPDUB51Pp2MwnOCHg0xMkRYMCtW2N3m7Gr38XS9Cql/j2cg952DN63tdGd1amSPvfsw83/ADkCCBPs3qmgb6eyOdtSfWMxU1q5ROlj4XxortvlgZmPUZhMW4fBYYi248LNIvPq1TKGNDIXHh8epFYom6rqLWIniRYNUosQv7xUH6gqOJ62+d+YDfN/z6+5eyiUvC8uZGBC6J2WKhg79Lr3MJi9N0dILy/57aSja080sOno8RiO3Ypod3m/k4T085U1Hq8oyMqJUvJvyLRKKkZyVfCnyckda0hNIXj+oGwPnVJso+UbusLFrsDuUjBK/Cg8xESexS70p3kEHiUoxGYmSf3M3VM0bmTBVUCPrlYtMmy6rd/6DG+BeLBGk6EeTGFs1W2p5JeitlDvMfwyQbt56PtpKlY=; SPC_EC=.ZDBTNlpaZk00aGEwaWlDM7Ab1FMw+MwUA9gAqNDsmZrKqUiwDI4Qtj7iQFLKOt8/qRAHaqpYK9ZPzaFPLhTOSN5BspUiFnp3XIZr2wQorsBu59Prrm4JUI7SpybW5Ec+2jFEIn7RBF01RKasmRaG38wOfuPD8lfa19EQT2mKjyOO6q77UymqhsfJfTz5/9/g/sLOh94lyrU6PRkOOhL2ud51EN16nQ5rqxGTL7urJhik6Cdml4mb2o+v4O4ePMc8; shopee_webUnique_ccd=9ksAHupK%2Bwlgr0nX8Yj8sw%3D%3D%7CJlkuACa6aFlZDpJM9dRd%2F3W7Uto69vkO6o9ZAi56ru%2BS9%2BjhB4SulLsLviSkM98KT0M478%2F5Uj5%2FkbPn0to%3D%7C3l2i%2FY9ZFRXhbx9V%7C08%7C3; ds=7a6b9866910bb4fb2c3ce32c876471ff"
        }

        response = requests.get(url, headers=headers, params=params).json()

        try:
            items = response['items']
        except:
            items = get_products_code()

        for item in items:
            url_detail = 'https://shopee.co.id/api/v2/item/get_ratings?exclude_filter=1&fe_toggle=&filter=0&filter_size=0&flag=1&fold_filter=0&itemid={}&limit={}&offset=0&relevant_reviews=false&request_source=2&shopid={}&tag_filter=&type=0&variation_filters='.format(
                item['itemid'], max_size, item['shopid'])
            headers_detail = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.9",
                "af-ac-enc-dat": "d8401485590ea685",
                "af-ac-enc-sz-token": "l9QwcxJzHBykTcqFkqGJmg==|elkuACa6aFlZDpJM9dRd/3W7Uto69vkO6o9ZAq7i3mmS9+jhB4SulLsLviSkM98KT0M478/5Uj5/kbPn0to=|3l2i/Y9ZFRXhbx9V|08|3",
                "content-type": "application/json",
                "priority": "u=1, i",
                "referer": "https://shopee.co.id/Apple-iPhone-13-128GB-Starlight-i.241308147.11764863710",
                "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Brave\";v=\"133\", \"Chromium\";v=\"133\")",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                "x-api-source": "pc",
                "x-csrftoken": "tcdPtojhQ164i9MJJIOF6uHiistvBZM7",
                "x-requested-with": "XMLHttpRequest",
                "x-sap-ri": "01bebe67a72f5c3d9846c53f05012c188d6d827a960d90c46876",
                "x-sap-sec": "CHFo24O/viMpWYyV8idV8Y7VNidJ8iSV1id78wYVskRG8m7VX9d68m9VwiQb8a4VCid28myV4idj8f7VZiRF8GoVaiRX8mSVU+dp8y4VPidx8G0VVidS8CdVgidr8a0VyiRr8g0VoiR/8w4VDiQA8m4VD+Rz8CyVA9RH8G4Va+Qu8GTVAkdX8iaVmiQR8jaVkiQU8idV8iQKrkdlRLAVWidV8idV863wOjTV+zViWi0V8iR39BM68kdV8idHAFiWeZT1ePOqS6eZhDd18iRxNMOpridV8YTU8idV8aXipKO89GUdMLqV8iYIE0glyHARnIA28idVCi7V8wdU8ic+Jvu+lEZ9u/HAr9kw8kdVMsFi5Z1McT5p8+dVzi7V8i6wMcHH8+dVAIgjn9dV8gr68+dVMi7V8idV8zmFUzdF8iQV1kdV8C2qr+Q6ti7V8ZrQjbiV8id1ki0V8iyV8iRdT/BMzmUCFadV8ickJLSBW0yYPc+L9WS5rrxzzty74PoOtEGuTmJarBzGwTtXiEXUifbjNUVLLL36Un0PHRKHE55nDXn2tp/QmnENgZRnwY1t27Sz16K/6wQv7nBbSeZxBtDnlsoWQtuIhm0nUMF1WLUHfBZqQGzyo23/j2arCy9+IsQ7xo+XaE7eBY5JU9hPcsYfO9V5DHUR6H00crDzsMWeX9SpCrgcGKbGDzpbLpdW/l8lpOO9wynnEZdZBIVUQQ7H4ivp+rqOCOkJ89dVVnQ+axuz/HQoHM8xW7rgrQtVmlUihRLjWHgVAn5BGWFwnIVsXPquAwwxK0eo2Rvm4Y/ZC119FKu/1zVwDy8vM8BkOm2djA05b4/ddJwXELeuqIgJc1f4uAf//LTE9E2AhUGCAqXhLDrUCViE0V2VbckX49rMnrH3YhX1h2GywYvl0dtCUhoORKmEx93okCF6QrsWH53QFGixgKmlZcWGvIWRNoQ3VNNFlnGgDt3CxR4/QWa/D5vBbK19dD0u2miU4uNLgSQPI0ySFB7PSWaEOEbNyqMAOwlWd+1C5pT/AC07dBpNjw0ry3cBQyusdG+SzJ8jmkR3ttLaHLMB3bAeLpDScpm/ws6NwdutPJBBSz6c8rlhdYVBciFT3nreRE6+NtMDjJ0WF4gWl+dVWidV8Z0zMAau8idVWYzd+i7V8iRXjkdV8+dV8yAD8idU8idViyYV8idV8idV8idV9idV8l5MWKh5lcXCbgyVekdV8idX8idVCm1tsEzGaApRViQ/8idV8gyV8idOZitEHR739f1OyLIc88RZqJoA0/qqURkPxAtp0kpslF50zvKMXQdtnf0Wet5YCASPnAcS2ik6m+dV8idp8idVnBrbLxVGv+SctRx7SXVsWOVKfGPr8P+yZB0FKGAbC9SPxAtH8idV8Y0V8idIgQXcVlXRwmzZjP2UbQ4Ix8HGmINa18XNCMNIxTNvG8HSfQAmfmRFi8jpmQ4OU5oKlF5OvMjLw4qLYPjmgDAIqP2CYA0duIb5gM5xxDAXZ4ALwA2Ii8iRj546i84KVfq0lDa0qIweml16xlq+ag2rUQiOz8jmfR6zwl6RVAHNUgzNUkd28idVcjdYON8w1s5r4sG7h7TfoQYX9kMXpn0ZY/CZXa8WdaquPZLp/qoDVn4NpxykSt/RC/qgs9dV8idA8idVDrH4Qo9/mPI=",
                "x-shopee-language": "id",
                "x-sz-sdk-version": "1.12.17"
            }

            response = requests.get(url_detail, headers=headers_detail).json()

            try:
                reviews = response['data']['ratings']
            except:
                reviews = get_product_reviews(max_size)
                break

        for review in reviews:
            comment = review['comment']
            timestamp = review['ctime']
            formatted_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

            print(review['author_username'])

            results.append({
                'user': review['author_username'],
                'timestamp': formatted_date,
                'rating': review['rating_star'],
                'content': comment,
                'preview': comment
            })
    else:
        results = []

    return results
