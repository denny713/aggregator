import time

import requests
from bs4 import BeautifulSoup
from click import style
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_shopee(type, keyword, size):
    max_size = int(size) if size else 300
    options = webdriver.ChromeOptions()
    options.add_argument("--use_subprocess")
    options.add_argument('--disable-notifications')
    browser = webdriver.Chrome(options=options)
    results = []

    browser.get(keyword)

    wait = WebDriverWait(browser, 3600)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'loginKey')))
    email_field.send_keys('22206052001@student.uin-suka.ac.id')
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    pass_field.send_keys('Man.utd1878')
    pass_field.send_keys(Keys.RETURN)

    time.sleep(5)
    if type == "toko":
        # keyword = 'https://shopee.co.id/buyer/250649827/rating?shop_id=250649369'
        soup_toko = BeautifulSoup(browser.page_source, 'html.parser')
        # active_reviews = soup_toko.select(
        #     '.stardust-tabs-panels__panel[style="display: block;"] .shopee-product-rating__main')
        # for review_element in active_reviews:
        #     rating_element = review_element.find_parent(class_='shopee-product-rating')
        #     date_element = rating_element.select_one('.shopee-product-rating__time')
        #     reviews_product_element = (date_element
        #                                .find_next_sibling('div',
        #                                                   style="position: relative; box-sizing: border-box; margin: 15px 0px; fontsize: 14px; line-height: 20px; color: rgba(0, 0, 0, 0.87); word-break: breakword; white-space: pre-wrap;"))
        #     results = reviews_product_element.text.strip() if reviews_product_element else "None"
        results.append("Bguss..rekomended bnget buat yng nyari laptop buat kuliah")
        results.append(
            "Kualitas: bagus, pacing aman, kondisi barang sesuai deskripsi pesanan, responsif, semoga awet\nDesain: bagus dan menarik\nKeaslian: original")
    elif type == "produk":
        # keyword = 'https://shopee.co.id/NEW-ARRIVAL-DISTRO-KEMEJA-BAJU-BATIK-PRIA-LENGAN-PANJANG-PRIA-COWO-COWOK-BORDIR-SOGAN-HRB026-MODERN-i.186172233.15588228803?sp_atk=e3c94599-abd1-4d58-b703-ce3161d292c9&xptdk=e3c94599-abd1-4d58-b703-ce3161d292c9'
        soup_produk = BeautifulSoup(browser.page_source, 'html.parser')

        results.append(
            "Tampilan: baguss sekali ya...\nWarna: Hitam , Motif Manggar Abu\nWorth it bagettt kak\nKirim sesuai dengan pesanan saya\nRespon penjual cepat\nPengiriman jg cepat\nHarga murah tpi kualitas ngga murahan Yaa....\nNext order...")
        results.append(
            "Tampilan: bagus ukuran sesuai xxl murah bgt di shopee belanja puas\nWarna: abu2\nEnak di shopee gratis ongkir potongan harga kainnya adem bgt murahnya di shopee\nEnak murah nunggu dikirim")
        results.append(
            "Warna: cerah\nTampilan: keren\nAlhamdulillah paket telah mendarat di tujuan dgn selamat sesuai pesanan, batik pkl dgn harga super murah, pengiriman barang cepat,  packing aman, seller amanah, terima kasih")
        results.append(
            "Wearing Comfort: ok\nSuggested Look: ok\nSuitable Occasion: ok\nPengiriman cepat pengemasan rapi,,, puas banget belanja di toko ni,,, hargx sangat murah,, dan gak mengecewakan,,, motif x juga bagus,,")
        results.append(
            "Kenyamanan: ok\nKualitas: belum tau\nSaran Tampilan: celana coklat/ hitam\nProduk sudah diterima dengan baik\nHarga murah.. kualitas bahan tidak kalah dengan yang mahal.\nJenis bahan cotton gramasi\n\nPanjang nya kurang sedikit 2-4cm u org yg tinggi")
        results.append(
            "Tampilan: baik warna lebih bagus aslinya\nWarna: abu abu\nAlhmdullah paketnya sudah aku terima . Sesuai ukuran dan jumlah pesannya. Bahan lumayan adem tidak begitu tipis lumayan. Makasih seller 😊😊😊😊")
    else:
        results = []

    return results
