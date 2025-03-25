def get_user_id():
    return "241313695"


def get_shop_id():
    return "241308147"


def get_products_code():
    items = []
    items.append({"itemid": "5276258018", "shopid": "241308147"})
    items.append({"itemid": "24671927847", "shopid": "150918529"})
    items.append({"itemid": "25688260631", "shopid": "304902524"})
    items.append({"itemid": "26801472709", "shopid": "28367850"})
    items.append({"itemid": "19690086989", "shopid": "28367850"})
    items.append({"itemid": "29305222731", "shopid": "27476373"})
    items.append({"itemid": "25460833813", "shopid": "28367850"})
    items.append({"itemid": "24407157243", "shopid": "1021187906"})
    items.append({"itemid": "25415760327", "shopid": "28367850"})

    return items


def get_product_reviews(size):
    results = []
    data = generate_product_reviews()
    limit = min(size, len(data))
    for x in range(limit):
        results.append(data[x])

    return results


def generate_product_reviews():
    return [{
        "itemid": 5276258018,
        "ctime": 1630809106,
        "userid": 116245082,
        "shopid": 241308147,
        "comment": "Kualitas produk sangat baik, packingan sangat aman dengan packing kayu sehingga tidak terjadi hal2 yg tidak diinginkan pada saat pengiriman berlangsung, admin ramah dan fast respon. Overall puas!",
        "rating_star": 5,
        "author_username": "bwnugroho"
    }, {
        "itemid": 5276258018,
        "ctime": 1681793183,
        "userid": 77328408,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:baterainya awet banget\n\nHarga sesuai karena materialnya premium banget, kokoh banget tiap sisi, cepet banget sat set sat set. Pas pengiriman kaget dan khawatir banget karna pas dateng dus di bungkus plastik tapi basah kuyup, tapi pas dibuka aman karna ada dilapis plastik lagi. Thanks",
        "rating_star": 5,
        "author_username": "kiramdanii"
    }, {
        "itemid": 24671927847,
        "ctime": 1739339894,
        "userid": 362272944,
        "shopid": 150918529,
        "comment": "Lumayan mantap...",
        "rating_star": 5,
        "author_username": "vaozee1"
    }, {
        "itemid": 5276258018,
        "ctime": 1683651595,
        "userid": 118003693,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:performa bagus\nSepadan dengan Harga:sesuai\n\nAlhamdulillah barang sampai dg aman, saya tdk pakai proteksi saat checkout, barang diantar langsung oleh kurir dr shopee, dan wajib yg bersangkutan yg menerima barangnya",
        "rating_star": 5,
        "author_username": "yuniapriliani_"
    }, {
        "itemid": 5276258018,
        "ctime": 1686941304,
        "userid": 17106156,
        "shopid": 241308147,
        "comment": "Alhamdulillah seneng banget macbooknya sampe dengan selamat. Deg2an takut knp2 soalnya jauh ke sulsel untungnya selamat ga ada cacat alhamdulillah. Pengiriman cepet. Pake protection dr shopee jd di packing kayu. Skrg pemakaian 1 minggu tetep oke. Thanks ibox 🙏🏽👍🏾👍🏾👍🏾👍🏾",
        "rating_star": 5,
        "author_username": "tabriiz.berkah"
    }, {
        "itemid": 5276258018,
        "ctime": 1630824698,
        "userid": 433518409,
        "shopid": 241308147,
        "comment": "Pembelian kedua kalinya di ibox ga pernah kecewa, admin yang ramah dan pengiriman juga cepat, kualitas produk sangat baik, produk juga original, harga produk sangat baik",
        "rating_star": 5,
        "author_username": "r*****g"
    }, {
        "itemid": 5276258018,
        "ctime": 1683428541,
        "userid": 514962209,
        "shopid": 241308147,
        "comment": "Sepadan dengan Harga:okay\nFitur Terbaik:okay\n\nAhhh sukaaa banget, awalnya takut mau beli lewat online tpi saya memberanikan diri dan alhamdulilah gada kendala apapun. Semoga awet",
        "rating_star": 5,
        "author_username": "alvinnavinavin2612"
    }, {
        "itemid": 5276258018,
        "ctime": 1696865703,
        "userid": 371361107,
        "shopid": 241308147,
        "comment": "Sepadan dengan Harga:cocok sama harga dah pokonya terjangkau\nFitur Terbaik:kualitas bguss jangan d ragukan lagi klo iBox mh\n\nProduk terbaik jangan ragu beli d iBox harga terjangkau pengiriman cepatt gooodd joobb pokonya dah kurirnya asik ramah bet puas dah pokonya 100%",
        "rating_star": 5,
        "author_username": "m*****k"
    }, {
        "itemid": 5276258018,
        "ctime": 1630252721,
        "userid": 5644682,
        "shopid": 241308147,
        "comment": "Pertama kalinya beli macbook online, sempet ragu-raug karena pengiriman jarak jauh. Untung sampai lebih cepat dari estimasi + di packing dengan aman banget. Sellernya juga ramah",
        "rating_star": 5,
        "author_username": "n*****i"
    }, {
        "itemid": 5276258018,
        "ctime": 1654702096,
        "userid": 63503673,
        "shopid": 241308147,
        "comment": "Macbook nya sudah sampai 🙂 Pengiriman cepat, seller responsif, barang dikirim dg shopee xpress instant sampai dengan aman. Kualitas nya mantapp. Thankyou ibox.",
        "rating_star": 5,
        "author_username": "meinda22"
    }, {
        "itemid": 5276258018,
        "ctime": 1655125401,
        "userid": 75111549,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:New Macbook Air jadi pengalaman baru yg luar biasa\nSepadan dengan Harga:Sesuai dengan kualitasnya\n\nRecomended untuk dibeli, terima kasih Seller. Tempat transaksi yg dipercaya.",
        "rating_star": 5,
        "author_username": "avinafisah"
    }, {
        "itemid": 5276258018,
        "ctime": 1616138233,
        "userid": 138217190,
        "shopid": 241308147,
        "comment": "Sangat memuaskan bagus banget Alhamdulillah sampai dengna selamat dan keadaan mulus luvvv banget pokoknya ❤❤❤❤✨✨",
        "rating_star": 5,
        "author_username": "melati.1.2"
    }, {
        "itemid": 5276258018,
        "ctime": 1663207113,
        "userid": 276733699,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:bagus\nSepadan dengan Harga:benar\n\nLaptop berfungsi baik..kondisi barang bagus tdk ada cacat msh tersegel baik nd bergaransi.\nPengiriman nd pengemasan aman cepat\nTrimaksh seller yg ramah ..",
        "rating_star": 5,
        "author_username": "9om2q6yg9c"
    }, {
        "itemid": 5276258018,
        "ctime": 1612354408,
        "userid": 286612389,
        "shopid": 241308147,
        "comment": "Sabtu malam pesan, minggu malam dikirim, senin sampe kota tujuan, selasa pagi dikirim ke tempat tujuan. \nSang pengirim shopee express naik mobil hatchback hitam, memastikan si penerima benar orangnya, data di resi difoto, penerima jg difoto sambil megang box paketnya.\nBarangnya oke dan tanpa kendala",
        "rating_star": 5,
        "author_username": "Pengguna Shopee"
    }, {
        "itemid": 5276258018,
        "ctime": 1629620827,
        "userid": 23048450,
        "shopid": 241308147,
        "comment": "Pesen jam 11.50, bayar jam 12.10an dan langsung dikirim pake kurir Instant jam 3 daan sampee jam 6 (karena sempet hujan deres bgt dan banyak daerah yg banjir juga) tp overall sukaaaabgt! Barang dipacking dgn aman dan kondisi juga amaan bgt box dan laptopnyaa. Admin juga ramah dan responsif, thank u!",
        "rating_star": 5,
        "author_username": "elinthnmsr"
    }, {
        "itemid": 5276258018,
        "ctime": 1647336717,
        "userid": 177675495,
        "shopid": 241308147,
        "comment": "Mantab, Respon cepat. Pengiriman cepat, barangnya bagus sesuaiii. Ada promo diskon 500k lagi. Awalnya kaget yang dateng gede banget, pake kayu, boxnya double2, gedenya bisa 3x box macbooknya 😂jelas amannyaa. 🙌 Macbooknya udah dipake beberapa jam, normal...",
        "rating_star": 5,
        "author_username": "sidiq_tc"
    }, {
        "itemid": 5276258018,
        "ctime": 1621994350,
        "userid": 63814465,
        "shopid": 241308147,
        "comment": "Paket datang dengan selamat, konfisi dipacking kayu terus dusnya dobel, ohiya kurirnya juga ramah, rekomended pokoknya toko ini 👍👍👍👍",
        "rating_star": 5,
        "author_username": "takultv"
    }, {
        "itemid": 5276258018,
        "ctime": 1711028714,
        "userid": 179488847,
        "shopid": 241308147,
        "comment": "Barang mendarat dengan selamat, fast response, sampai tepat waktu sesuai dengan estimasi, packing nya bagus menggunakan kayu safety jd tidak takut dalamnya penyok. Sudah dicoba tidak ada kendala recommended deh tidak diragukan!",
        "rating_star": 5,
        "author_username": "arbain.akbar"
    }, {
        "itemid": 5276258018,
        "ctime": 1620149074,
        "userid": 14902886,
        "shopid": 241308147,
        "comment": "keren bgt packing kayu jugaa aaaa cmn memang rada lama tp thankyou sampai selamat sentosa. macbooknya jg kerenbgt 🥺💕",
        "rating_star": 5,
        "author_username": "k*****n"
    }, {
        "itemid": 5276258018,
        "ctime": 1681898535,
        "userid": 24317356,
        "shopid": 241308147,
        "comment": "Sepadan dengan Harga:Alhamdulillah\nFitur Terbaik:Very good service and product\n\nRecommended pokoknya",
        "rating_star": 5,
        "author_username": "n*****n"
    }, {
        "itemid": 5276258018,
        "ctime": 1724468594,
        "userid": 131315964,
        "shopid": 241308147,
        "comment": "Keaslian:asli\nKualitas:baik\nKegunaan:untuk pakai kerja\n\nPesanan udah sampai dan sesuai.. Pengiriman cepat.. Packing super aman pakai peti kemas.. Keren macbook nya.. Sesuai pesanan.. Semoga awet dan tahan lama.. Makasih ya seller..",
        "rating_star": 5,
        "author_username": "y*****4"
    }, {
        "itemid": 5276258018,
        "ctime": 1615387999,
        "userid": 60380645,
        "shopid": 241308147,
        "comment": "Alhamdulillah sampai dengan selamat walau ga dipacking kayu. Pengiriman cepat, 1 hari sampai. Terima kasih",
        "rating_star": 5,
        "author_username": "lahtyhan"
    }, {
        "itemid": 5276258018,
        "ctime": 1631588289,
        "userid": 61669338,
        "shopid": 241308147,
        "comment": "Mantaplahhh, awalnya sedih bamget karna gadapet warna gold. But space grey is beautiful color tooo. And im in lobe with it. Thankyou iboxxx.",
        "rating_star": 5,
        "author_username": "erichaocta"
    }, {
        "itemid": 5276258018,
        "ctime": 1630392199,
        "userid": 154781779,
        "shopid": 241308147,
        "comment": "Produknya bagus sampainya cepet banget. Di packing juga rapi banget. Adminnya ramah” semua. Thank you ya",
        "rating_star": 5,
        "author_username": "greythama"
    }, {
        "itemid": 5276258018,
        "ctime": 1697961394,
        "userid": 439775976,
        "shopid": 241308147,
        "comment": "Sepadan dengan Harga:barang oke sesuai harga nya\nFitur Terbaik:cukup baik\n\nBarang sampai dengan selamat tidak kurang dan kurir ramah sampai di bantu bukain buat mastiin barang nya aman ...",
        "rating_star": 5,
        "author_username": "a*****i"
    }, {
        "itemid": 5276258018,
        "ctime": 1740737703,
        "userid": 44547491,
        "shopid": 241308147,
        "comment": "Keaslian:asli\nKualitas:terbaik\nKegunaan:bikin digital content\n\nPackingnya juara bgt, sampe panik sendiri pas terima karna aku tinggal sendiri dan ga punya palu. Akhirnya berusaha sendiri buka pake sendok dan bisa haha 😂\nBarang aman original, pas dinyalakan langsung garansi aktif satu tahun dan dapat free apple tv dan apple music 3 bulan 👍🏻\n\nKualitas dan fitur ga usah ditanya, smoooothh bgt emang macbook satu ini 🫶🏻 ringan tipis, cakep banget buat dibawa wfc-an, suara jerniiihh bgt, kamera kinclong bgt dipake zoom call langsung auto glowing asli 😍",
        "rating_star": 5,
        "author_username": "whatdewisays"
    }, {
        "itemid": 5276258018,
        "ctime": 1681651990,
        "userid": 217421670,
        "shopid": 241308147,
        "comment": "Sepadan dengan Harga:harga sepadan dengan kualitas barang\n\nPackaging dengan kayu, sampai di rumah dengan kondisi baik. Pengiriman cepat, pesan jam 12 siang hari jumat sampai di rumah jam 5 sore hari minggu.",
        "rating_star": 5,
        "author_username": "s*****i"
    }, {
        "itemid": 5276258018,
        "ctime": 1652616702,
        "userid": 54564259,
        "shopid": 241308147,
        "comment": "kualitas produk sangat baik dan barang original pengirimannya super cepat  terpercayaa!!! \nwalaupun genemu kartu garansinya",
        "rating_star": 5,
        "author_username": "ratunf01"
    }, {
        "itemid": 5276258018,
        "ctime": 1644930196,
        "userid": 10543521,
        "shopid": 241308147,
        "comment": "Produk original. Diterima dengan baik. Pengemasan sangat mantap dengan tambahan kayu. Pengiriman ok, kurir sip.",
        "rating_star": 5,
        "author_username": "abifatah"
    }, {
        "itemid": 5276258018,
        "ctime": 1724673675,
        "userid": 35089219,
        "shopid": 241308147,
        "comment": "Keaslian:terjamin asli\nKualitas:bagus daripada yg lainnya\n\nBagus produknya. \nBaru pertama kali beli online, agak worry sih\nTapi emang mantab bgt ini ibox online\nPengirimannya pakai kayu",
        "rating_star": 5,
        "author_username": "d*****3",
    }, {
        "itemid": 5276258018,
        "ctime": 1678965964,
        "userid": 136811757,
        "shopid": 241308147,
        "comment": "Saya sangat kecewa dengan Ibox Indonesia. Saya beli Macbook itu tidak murah dan ini jelas jelas barang elektronik dimna lokasi rumah sy juauh di ujung pulau jawa n ibox di jkt. Itu sgt jauh, udah chat kalo request packing kayu tapi katanya tergantung ekspedisi. Dan packing pakek bubble wrap dan perlindungan apa gt katanya. Nyatanya sampe dirumah setelah 7 hari itu bener bener hanya kotak coklay doang tanpa bubble wrap dan packing kayu. Padahal di invoice udah tertulis packing kayu, bukti ada digambar, silahkan di analisis. Saya chat komplain setelah barabg datang katanya memang tergantung pihak ekspedisi, akhirnya saya chat komplain ke pihak ekspedisi shopee express katanya semua kendala dikembalikan ke pihak toko. Gimana tuh ibox, ayo dong hargai pembeli nya. \nKata nya silahkan di unbox pakek video n jika ada keluhan bisa disampaikan, nah masalahnya elektronik itu kalo ke geser atau kena apa gt fisik nya oke oke aja tapi kan gaktau dalemnya, dan biasanya muncul kalo udah dipakek. Gmna bisa mengetahui masalah dalam 24 jam doang, gmna cara berfikirnya? \nDan belum ribet pula prosesnya. Saya bener bener heran dan shock, saya baru pertama beli di ibox dan trauma, saya hanya bisa berdoa semoga macbook ini gak ada masalah kedepannya. Karena uang segitu saya nabung bertahun2 dan gak mudah bagi saya. Ibox pelayanannya sangat mengecawakan, padahal distributor resmi apple, astaga. Sangat sedih rasanya, kesel dan sedih itu gak bisa digantikan, shock kaget liat barang datang cuma kardus doang tanpa perlindungan.",
        "rating_star": 1,
        "author_username": "o*****_"
    }, {
        "itemid": 5276258018,
        "ctime": 1647321695,
        "userid": 69425054,
        "shopid": 241308147,
        "comment": "degdegan awalnya mau beli via shopee, tp karena situasi jd harus memberanikan diri, alhamdulillah ternyata tiba dari jkt ke bandung dengan selamat, packing super aman! cuma 3 hari an udh sampe. Thankyou ibox👏🏻👏🏻",
        "rating_star": 5,
        "author_username": "y*****3"
    }, {
        "itemid": 5276258018,
        "ctime": 1657905923,
        "userid": 123490070,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:terbaik\nSepadan dengan Harga:harga sangat sesuai\n\nMacbook air M1 juara,,,aslinya mau nunggu M2 tapi kelamaan yadah beli M1 jg gpp, barang bagus dan sangat mulus walau gak di packing kayu padahal kirimnya ke luar jawa,,,pemakaian sudah mau masuk 1 bulan semua kondisi aman baterai awet tahan lama,beli pas diskon cashback 1 jt dan harga asli 16 jt",
        "rating_star": 5,
        "author_username": "i*****0"
    }, {
        "itemid": 5276258018,
        "ctime": 1703438257,
        "userid": 33655237,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:M1 Chipset\nSepadan dengan Harga:Sepadan daripada M2/M3\n\nSaya memilih ini akrena kecepatan penulisan data yang lebih cepat dari versi terbarunya (M2/M3) dengan kapasitas SSD yang sama.\n\nAlasan utamanya jelas budgetnya hanya segini. Tentu masih bisa digunakan untuk mengedit kepentingan video sosmed secara dasar, tentunya sangat power full sekali untuk menyelesaikan pekerjaan yang kaitannya tidak jauh dari dokumen. Sisanya ini lebih dari cukup untuk enterainmet dan companion Apple Ecosystem saya",
        "rating_star": 5,
        "author_username": "Pengguna Shopee"
    }, {
        "itemid": 5276258018,
        "ctime": 1709620242,
        "userid": 66741943,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:💙💙💙\nSepadan dengan Harga:Sepadan\n\nAlhamdulillah paketnya sampai dengan selamat, sesuai dengan pesanan, packingnya juga aman banget pakai kayu, rapih juga pokoknya mantap. Makasih banyaaak seller ibox dan kurir. 💙",
        "rating_star": 5,
        "author_username": "f*****t"
    }, {
        "itemid": 5276258018,
        "ctime": 1628116392,
        "userid": 6437659,
        "shopid": 241308147,
        "comment": "Barang diterima dgn baik. Pengiriman cepat. Respon cs nya jg ramah, cepat & jelas. Rekomen lgsg beli di ibox nya, harga ok. Thank youu",
        "rating_star": 5,
        "author_username": "s*****u"
    }, {
        "itemid": 5276258018,
        "ctime": 1685511042,
        "userid": 718467608,
        "shopid": 241308147,
        "comment": "Kualitas bahan premium dan value for money.\nCompact dan ringan.",
        "rating_star": 5,
        "author_username": "x*****d"
    }, {
        "itemid": 5276258018,
        "ctime": 1615860835,
        "userid": 37278393,
        "shopid": 241308147,
        "comment": "Pesan pagi, sore sudah dikirim dan besoknya udh sampe. Pengiriman cepat, packaging aman, seller juga responsif. Overall puas sih. Terima kasih. ",
        "rating_star": 5,
        "author_username": "n*****i"
    }, {
        "itemid": 5276258018,
        "ctime": 1683019687,
        "userid": 75341066,
        "shopid": 241308147,
        "comment": "Fitur Terbaik:Os\nSepadan dengan Harga:Sepadan\n\nAdmin oke, sempat ganti warna, dan dibantu dengan baik. Pengiriman menggunakan packing kayu. Dan hanya 4 hari sudah sampai. 👍🏼👍🏼",
        "rating_star": 5,
        "author_username": "n*****m"
    }, {
        "itemid": 5276258018,
        "ctime": 1625437831,
        "userid": 39779109,
        "shopid": 241308147,
        "comment": "Pesanannya diproses cepet banget sehari sampe, produk jangan ditanya lah pasti original dan bagus",
        "rating_star": 5,
        "author_username": "r*****1"
    }, {
        "itemid": 5276258018,
        "ctime": 1689049934,
        "userid": 303670713,
        "shopid": 241308147,
        "comment": "design sleek, kualitas oke, worth it bangett semoga bisa ngelancarin kerjaan. saran buat penjual mungkin bisa diversifikasi jasa kirim soalnya jne lemot banget",
        "rating_star": 5,
        "author_username": "r*****l"
    }, {
        "itemid": 5276258018,
        "ctime": 1650872114,
        "userid": 283166233,
        "shopid": 241308147,
        "comment": "Sudah pasti puas belanja di iBox. Asli produknya dan mantab layananya. Meski menjelang lebaran paket sampai dgn cepat. Terimakasih.",
        "rating_star": 5,
        "author_username": "d*****e"
    }, {
        "itemid": 5276258018,
        "ctime": 1618140667,
        "userid": 28173013,
        "shopid": 241308147,
        "comment": "asli sih baru checkout siang tgl 10, tgl 11 sore udh dateng, alhamdulillah bisa buat ujian❤️ hehe yang baca mohon doanya yah! ",
        "rating_star": 5,
        "author_username": "soshicaramel"
    }, {
        "itemid": 24671927847,
        "ctime": 1732694244,
        "userid": 14180221,
        "shopid": 150918529,
        "comment": "Fungsi:fungsi semua\nKondisi Barang:Baik berjalan lancar\n\nSpesifikasi sesuai, tapi yang tidak sesuai ccycel count nya beda aama foto, di foto maaih 160 an tapi yang datang dah 360 an...",
        "rating_star": 5,
        "author_username": "sanzer7"
    }, {
        "itemid": 24671927847,
        "ctime": 1737519328,
        "userid": 866990186,
        "shopid": 150918529,
        "comment": "Kondisi:Sangat Bagus\nFungsi:Baik\nSpesifikasi:sesuai\n\nmasih ada garansi 30 hari. lagi tahap pemakaian.\nsemoga tidak terjadi kendala yg berarti.Makasi",
        "rating_star": 5,
        "author_username": "balcksweet84"
    }, {
        "itemid": 24671927847,
        "ctime": 1739339894,
        "userid": 362272944,
        "shopid": 150918529,
        "comment": "Lumayan mantap...",
        "rating_star": 5,
        "author_username": "vaozee1"
    }, {
        "itemid": 24671927847,
        "ctime": 1739444859,
        "userid": 216716280,
        "shopid": 150918529,
        "comment": "Kondisi:ok",
        "rating_star": 5,
        "author_username": "yantisuhsrti"
    }, {
        "itemid": 24671927847,
        "ctime": 1742342265,
        "userid": 963764753,
        "shopid": 150918529,
        "comment": "Mantop !!!",
        "rating_star": 5,
        "author_username": "leejames978"
    }, {
        "itemid": 25688260631,
        "ctime": 1739951350,
        "userid": 1319988327,
        "shopid": 304902524,
        "comment": "Kegunaan:Good seller barang sampai dengan selamat, bubble wrap tebal ++, aman ga terjadi apa2😍\nKeaslian:Asli pastinya mantap 😍\nKondisi:overall good dari packingannya, kurirnya aman. Bintang 5😊\n\njangan ragu belanja disini",
        "rating_star": 5,
        "author_username": "yuushan042"
    }, {
        "itemid": 25688260631,
        "ctime": 1738692220,
        "userid": 820693,
        "shopid": 304902524,
        "comment": "Aku beli macbook dan iphone pas event 2.2\nPengiriman cepat, packing rapih, seller responsif, cuma agak nyesel beli hp di harga 12.1 ternyata besoknya turun jd 11.5",
        "rating_star": 5,
        "author_username": "ray._.store"
    }, {
        "itemid": 25688260631,
        "ctime": 1736770889,
        "userid": 96244021,
        "shopid": 304902524,
        "comment": "Keaslian:cek garansi aktif\nKualitas:bagus\nKondisi Barang:bagus\n\nRekomended",
        "rating_star": 5,
        "author_username": "jenrinaldo"
    }, {
        "itemid": 24671927847,
        "ctime": 1739339894,
        "userid": 362272944,
        "shopid": 150918529,
        "comment": "Lumayan mantap...",
        "rating_star": 5,
        "author_username": "vaozee1"
    }, {
        "itemid": 25688260631,
        "ctime": 1735573112,
        "userid": 1374608091,
        "shopid": 304902524,
        "comment": "barang ori, bagus",
        "rating_star": 5,
        "author_username": "faisalyudo"
    }, {
        "itemid": 25688260631,
        "ctime": 1737683426,
        "userid": 106600391,
        "shopid": 304902524,
        "comment": "Terima kasih banyak",
        "rating_star": 5,
        "author_username": "muzziku"
    }, {
        "itemid": 25688260631,
        "ctime": 1737526956,
        "userid": 273188971,
        "shopid": 304902524,
        "comment": "Sesuai",
        "rating_star": 5,
        "author_username": "alleyway88"
    }, {
        "itemid": 25688260631,
        "ctime": 1742684259,
        "userid": 178581259,
        "shopid": 304902524,
        "comment": "Admin fast respon dan garcep dalam membalas chat , overall pelayanan sangat oke,puas dan mantap",
        "rating_star": 5,
        "author_username": "fadillkusuma"
    }, {
        "itemid": 25688260631,
        "ctime": 1741226534,
        "userid": 98850587,
        "shopid": 304902524,
        "comment": "Kegunaan:MBP M4 Pro\nKeaslian:Garansi Inter\nKondisi:Baik\n\nSamapi dengan selamat walau di sudut box ada penyok mungkin karena ekspedisi karena hanya menggunakan buble warp tanpa ada opsi pilihan packing kayu.\nLeptop didalam dan kelengkapan aman, Terimakasih",
        "rating_star": 5,
        "author_username": "kadekendras"
    }, {
        "itemid": 25688260631,
        "ctime": 1741178186,
        "userid": 142310195,
        "shopid": 304902524,
        "comment": "Berfungsi dgn baik",
        "rating_star": 5,
        "author_username": "ferdonio_damanik"
    }, {
        "itemid": 25688260631,
        "ctime": 1736793693,
        "userid": 381467366,
        "shopid": 304902524,
        "comment": "Keaslian:Yah Asli ⭐️⭐️⭐️⭐️⭐️⭐️\nKualitas:Apple ⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️\nKondisi Barang:Aman Packing Tebal ⭐️⭐️⭐️⭐️⭐️⭐️",
        "rating_star": 5,
        "author_username": "amorasdk"
    }, {
        "itemid": 26801472709,
        "ctime": 1735721254,
        "userid": 8488883,
        "shopid": 28367850,
        "comment": "Kondisi Barang:mulus 90%\nKualitas:sangat baik\nSpesifikasi:macbook pro\n\nHarga murah terjangkau\nNext saya order lagi kak yg core i7\nTerima kasih kak \nJangan ragu beli di sini \nPenjual Recommended\nSukses selalu kak",
        "rating_star": 5,
        "author_username": "gcclothingindonesia"
    }, {
        "itemid": 26801472709,
        "ctime": 1734870617,
        "userid": 354487172,
        "shopid": 28367850,
        "comment": "Fungsi:sesuai\nKondisi Barang:baik mulus\nSpesifikasi:sesuai deskripsi\n\nAlhamdulilh barang sesuai... \nKualitasnya bagus... Selama uji coba 3 hari smua lancar tanpa kendala... Batrai awet... \nSellernya ramah... Trimakasi\nJangan ragu beli di sini",
        "rating_star": 5,
        "author_username": "lucky_lookfishfam"
    }, {
        "itemid": 26801472709,
        "ctime": 1734927465,
        "userid": 1132506335,
        "shopid": 28367850,
        "comment": "Fungsi:Bagus\nKondisi Barang:mulus laksana baru\n\nSeller aman",
        "rating_star": 5,
        "author_username": "mecomputers"
    }, {
        "itemid": 26801472709,
        "ctime": 1740461454,
        "userid": 13063735,
        "shopid": 28367850,
        "comment": "Kondisi Barang:awal datang sih aman aja walo ada komplen kedap kedip dilayar katanya truetone itu\nKualitas:oke\nSpesifikasi:oke\n\nBarangnya belum sebulan dipake tp LCDnya rusak. Kita disalahin krna gamake dengan baik pdahal macbook dijaga banget, blm dipake mobile kmana2, dan gaada garansi juga, dahlah. Sebagai pengguna macbook hampir 9 tahun, dan ini beli lagi, ini zonk sih. Males banget. Ga lagi lagi",
        "rating_star": 2,
        "author_username": "helloanina"
    }, {
        "itemid": 26801472709,
        "ctime": 1739793600,
        "userid": 189707176,
        "shopid": 28367850,
        "comment": "Kondisi Barang:95%\nKualitas:baik\nSpesifikasi:oke\n\nSemoga awet… pengiriman cepat",
        "rating_star": 5,
        "author_username": "syifasafianingtias11"
    }, {
        "itemid": 26801472709,
        "ctime": 1737888176,
        "userid": 742455444,
        "shopid": 28367850,
        "comment": "Kondisi Barang:bagus\nKualitas:bagus\nSpesifikasi:bagus\n\nPengiriman JNE lamaaaaa",
        "rating_star": 5,
        "author_username": "zha_ozha"
    }, {
        "itemid": 26801472709,
        "ctime": 1729521183,
        "userid": 26096329,
        "shopid": 28367850,
        "comment": "Fungsi:Oke\nKondisi Barang:Oke meski ada dent kecil\nSpesifikasi:MBP 2020 i7\n\nSeneng banget Seller ramah... barang aman ga ada kendala",
        "rating_star": 5,
        "author_username": "vangkecrew"
    }, {
        "itemid": 26801472709,
        "ctime": 1741645685,
        "userid": 82892073,
        "shopid": 28367850,
        "comment": "Kondisi Barang:Mulus 97%\nKualitas:Sangat Baik\nSpesifikasi:i7 32gb\n\nTerima kasih seller!!",
        "rating_star": 5,
        "author_username": "r*****a"
    }, {
        "itemid": 26801472709,
        "ctime": 1735539934,
        "userid": 1011788288,
        "shopid": 28367850,
        "comment": "overall bagus, sesuai dengan harga",
        "rating_star": 5,
        "author_username": "f*****1"
    }, {
        "itemid": 26801472709,
        "ctime": 1742035107,
        "userid": 906398011,
        "shopid": 28367850,
        "comment": "Kondisi Barang:Datang dengan baik\nKualitas:bagus\nSpesifikasi:mantap",
        "rating_star": 5,
        "author_username": "artadyagumelar"
    }, {
        "itemid": 26801472709,
        "ctime": 1731064665,
        "userid": 12745833,
        "shopid": 28367850,
        "comment": "Penjualnya bagus tapi barangny ada yg lecet 🙏🏻",
        "rating_star": 4,
        "author_username": "annisasilvianovianti"
    }, {
        "itemid": 19690086989,
        "ctime": 1728496296,
        "userid": 640901364,
        "shopid": 28367850,
        "comment": "Kondisi Barang:bagusss dan lumayan mulus 95%\nKualitas:sejauh ini bagus\nSpesifikasi:baguss\n\nBarang sesuai deskripsi dan pelayanan dr seller juga baik sekali dan fast respond! Sangat terpercaya",
        "rating_star": 5,
        "author_username": "putrimdew29"
    }, {
        "itemid": 19690086989,
        "ctime": 1731686269,
        "userid": 141651279,
        "shopid": 28367850,
        "comment": "Keandalan:Baik\nKondisi Barang:Bekas 95% msih mulus bngat\nKualitas:Kualitas gak perlu di ragukan",
        "rating_star": 5,
        "author_username": "frendyglaude"
    }, {
        "itemid": 19690086989,
        "ctime": 1733379585,
        "userid": 129825033,
        "shopid": 28367850,
        "comment": "Keandalan:Produk Original\nKondisi Barang:Datang Dalam Keadaan Mulus\nKualitas:Kuliatas Grade A\n\nBarang mulus, sedikit lecet pemakaian wajar, MacOS terbaru, dibantu installkan adobe family dan Office, harga terjangkau sesuai kondisi👍🏻",
        "rating_star": 5,
        "author_username": "ramandikaputra123"
    }, {
        "itemid": 19690086989,
        "ctime": 1725460748,
        "userid": 149052824,
        "shopid": 28367850,
        "comment": "Kondisi Barang:Normal, bekas pemakaian\nKualitas:Lumayan untuk harga segini\n\nMantap. So far so good untuk pemakaian daily. Semoga Awet.",
        "rating_star": 5,
        "author_username": "s*****7"
    }, {
        "itemid": 19690086989,
        "ctime": 1739791330,
        "userid": 39060588,
        "shopid": 28367850,
        "comment": "Kondisi Barang:Bagus\nKeandalan:Baik\nKeaslian:bagus\n\nBarang diterima sangat baik dan bagus meskipun bekas, no dent dan aman pemakaian selama ini. Moga2 bertahan sampai tahun esok",
        "rating_star": 5,
        "author_username": "n*****a"
    }, {
        "itemid": 19690086989,
        "ctime": 1734512573,
        "userid": 62199305,
        "shopid": 28367850,
        "comment": "Kondisi Barang:sesuai dengan negosiasi saat chat\n\nSemoga awet dan bermanfaat",
        "rating_star": 5,
        "author_username": "gonzagadika"
    }, {
        "itemid": 19690086989,
        "ctime": 1724077154,
        "userid": 32510210,
        "shopid": 28367850,
        "comment": "Fitur Terbaik:keren bener\nSepadan dengan Harga:oke\n\nSeller ramah, setiap nanya responnya cepat, barangnya masih mulus banget",
        "rating_star": 5,
        "author_username": "k*****1"
    }, {
        "itemid": 19690086989,
        "ctime": 1741146195,
        "userid": 234092991,
        "shopid": 28367850,
        "comment": "Kondisi Barang:good\nKeandalan:good\nKeaslian:Inter\n\nPemakaian 2 hari sejauh ini aman, dan tidak ada kendala, macnya mulus dan minim dent, dapet BH mac di 88%",
        "rating_star": 4,
        "author_username": "elgarbepo"
    }, {
        "itemid": 29305222731,
        "ctime": 1728036191,
        "userid": 327419656,
        "shopid": 27476373,
        "comment": "Fungsi:berfungsi dengan baik\nKondisi Barang:sesuai yg di sampaikan mimin, kondisi fisik 95% ok, bisa dibilang mulus banget untuk seri 2020. puas liat barang nya dan kondisi nya,",
        "rating_star": 5,
        "author_username": "s3sulawesi"
    }, {
        "itemid": 29305222731,
        "ctime": 1725116589,
        "userid": 177444063,
        "shopid": 27476373,
        "comment": "Fungsi:cukup normal\nKondisi Barang:cukup mulus\nSpesifikasi:sesuai\n\nCukup puas baik barang dan bubble warp yang dipakai. Thanks",
        "rating_star": 5,
        "author_username": "fadel_muhammad00"
    }, {
        "itemid": 29305222731,
        "ctime": 1727948918,
        "userid": 331894221,
        "shopid": 27476373,
        "comment": "Fungsi:berfungsi dengam baik\nKondisi Barang:mulus poll\nSpesifikasi:mbp\n\nPelayanannya bagus...rekomended toko...diskusonya juga mantab...",
        "rating_star": 5,
        "author_username": "jansennic"
    }, {
        "itemid": 29305222731,
        "ctime": 1727935622,
        "userid": 260307806,
        "shopid": 27476373,
        "comment": "Fungsi:Berjalan dengan baik\nKondisi Barang:Perfect\nSpesifikasi:Mantap Cocok buat jalanin banyak vm",
        "rating_star": 5,
        "author_username": "_icad"
    }, {
        "itemid": 29305222731,
        "ctime": 1727693541,
        "userid": 448593225,
        "shopid": 27476373,
        "comment": "Fungsi:baguss bgt masih mulusss",
        "rating_star": 5,
        "author_username": "dimaaspww"
    }, {
        "itemid": 25460833813,
        "ctime": 1728272513,
        "userid": 234332804,
        "shopid": 28367850,
        "comment": "Permukaan:sangat mulus\nKondisi Barang:sumpah baru\nKenyamanan:belanja di toko ini sangat luas\n\nmenyenangkan kali belanja disini , toko nya sangat ramahh, toko nya juga amanah, macbook nya baru ya kak ya Allah enak amanahhh sekali, sukses selalu buat toko nya, next time upgrade ke mac m2 disini aamiin hehe.. terima kasihhhh 🙏🏻🙏🏻",
        "rating_star": 5,
        "author_username": "dimaswahyupratama"
    }, {
        "itemid": 25460833813,
        "ctime": 1731667925,
        "userid": 8829198,
        "shopid": 28367850,
        "comment": "Permukaan:Like New\nKondisi Barang:cukup baik\nKenyamanan:cukup nyaman\n\nUnit Second yang sangat prefect baik OS maupun Hardware sangat layak pakai, tes rendering panas sangat stabil dan fan heatsink sangat bersih, tinggal pakai dan perawatan selanjutnya, Thank's untuk penjual",
        "rating_star": 5,
        "author_username": "ir.andika"
    }, {
        "itemid": 25460833813,
        "ctime": 1734384993,
        "userid": 260311921,
        "shopid": 28367850,
        "comment": "Permukaan:mulus\nKondisi Barang:berfungsi lancar\nKenyamanan:nyaman\n\nLumayan bagus mulus ada dent sedikit di sudut kanan kiri aja, dpt cc (3)  , imei tembus layar mulus semoga awet lah, btrai bertahan 1jam an untuk install\" Dan coba edit\" .. Harga nya worthit!",
        "rating_star": 5,
        "author_username": "22musicprod"
    }, {
        "itemid": 25460833813,
        "ctime": 1735600627,
        "userid": 1107749001,
        "shopid": 28367850,
        "comment": "Permukaan:Mulus Like New\nKondisi Barang:Sesuai dengan yang di Foto sebelum di kirim Mantap\nKenyamanan:Enak banget di pakainya nyaman\n\nRecommended, Adminnya ramah fast respons. Barangnya mulus seperti baru thankyou ... ⭐⭐⭐⭐⭐",
        "rating_star": 5,
        "author_username": "ceumilinceumilan"
    }, {
        "itemid": 25460833813,
        "ctime": 1719549304,
        "userid": 21072814,
        "shopid": 28367850,
        "comment": "Fungsi:bagus semuaa\nKondisi Barang:mulusss okee\n\nadmin nya fast respon",
        "rating_star": 5,
        "author_username": "tiszarizky"
    }, {
        "itemid": 25460833813,
        "ctime": 1731450818,
        "userid": 21198746,
        "shopid": 28367850,
        "comment": "Permukaan:mulus like new\nKondisi Barang:masih worth it\n\nMasih oke bgt smoga awet",
        "rating_star": 5,
        "author_username": "migrasi.jauh"
    }, {
        "itemid": 25460833813,
        "ctime": 1737748928,
        "userid": 42193417,
        "shopid": 28367850,
        "comment": "terimakasih saller. laptop langsung diajak kerjaaa... @hcproject21",
        "rating_star": 5,
        "author_username": "hc.project21"
    }, {
        "itemid": 25460833813,
        "ctime": 1737778426,
        "userid": 23591874,
        "shopid": 28367850,
        "comment": "Permukaan:mulus\nKondisi Barang:baik\nKenyamanan:nyaman\n\nMantap, semoga awet",
        "rating_star": 5,
        "author_username": "faturmarhas88"
    }, {
        "itemid": 25460833813,
        "ctime": 1731888473,
        "userid": 88985785,
        "shopid": 28367850,
        "comment": "Permukaan:mulus seperti baru\nKondisi Barang:bagus works all normal\nKenyamanan:nyaman, enak, mantep dahh\n\npenjual responsif dan cepat, baik juga pelayanan nya. mereka sabar serta komunikatif.",
        "rating_star": 5,
        "author_username": "h*****h"
    }, {
        "itemid": 25460833813,
        "ctime": 1734389309,
        "userid": 112804509,
        "shopid": 28367850,
        "comment": "Mantap min rekomend, admin responsif",
        "rating_star": 5,
        "author_username": "wildaariffaisal"
    }, {
        "itemid": 25460833813,
        "ctime": 1731417484,
        "userid": 52727322,
        "shopid": 28367850,
        "comment": "Permukaan:mulus\nKondisi Barang:benar2 istimeawa\nKenyamanan:oke\n\nMaaf baru review soalnya baru buka shopee",
        "rating_star": 5,
        "author_username": "muhammadyuswani"
    }, {
        "itemid": 25460833813,
        "ctime": 1738416599,
        "userid": 70761434,
        "shopid": 28367850,
        "comment": "Mantap untuk harga segitu lah mantap adminnya ge ramah tapi belum di coba tapi kasih bintang 5 dulu laaa",
        "rating_star": 5,
        "author_username": "fathir43store"
    }, {
        "itemid": 25460833813,
        "ctime": 1736732498,
        "userid": 48036336,
        "shopid": 28367850,
        "comment": "Goresannya banyak banget ternyata, but its okey, selagi fungsinya aman",
        "rating_star": 5,
        "author_username": "munadiyaah"
    }, {
        "itemid": 25460833813,
        "ctime": 1719728950,
        "userid": 222868540,
        "shopid": 28367850,
        "comment": "Adminnya ramah sekali, super duper baik. Aku jadi tidak enak habis komplain minta refund :(\nTerimakasih banyaakkk, semoga yang ini awet",
        "rating_star": 5,
        "author_username": "sunrithm"
    }, {
        "itemid": 25460833813,
        "ctime": 1738718693,
        "userid": 992315867,
        "shopid": 28367850,
        "comment": "bagus, aman sampai tujuan.",
        "rating_star": 5,
        "author_username": "m*****a"
    }, {
        "itemid": 25460833813,
        "ctime": 1717994195,
        "userid": 10310995,
        "shopid": 28367850,
        "comment": "Fungsi:Baik\nKondisi Barang:Cukup Baik\n\nBaik",
        "rating_star": 5,
        "author_username": "w*****n"
    }, {
        "itemid": 25460833813,
        "ctime": 1721257322,
        "userid": 34885647,
        "shopid": 28367850,
        "comment": "Mulus, sejauh ini aman nyaman lancar jaya!",
        "rating_star": 5,
        "author_username": "sifanggra"
    }, {
        "itemid": 25460833813,
        "ctime": 1727147082,
        "userid": 66188105,
        "shopid": 28367850,
        "comment": "Permukaan:mulus, minim baret\nKondisi Barang:sangat sangat sesuai ekspetasi!\nKenyamanan:berfungsi dengan lancar\n\nBener bener ga nyangka kalau ini second karena unitnya masih bagus sekali. Ram dan memori sesuai dengan yang tertera. Dapat warna yang dimau juga (grey) Seller sangat responsif. Semoga aja awet dan tahan lama. Semua fitur berfungsi dan mulu. Thank you seller and trusted! ✨️",
        "rating_star": 5,
        "author_username": "o*****y"
    }, {
        "itemid": 25460833813,
        "ctime": 1716516961,
        "userid": 301831641,
        "shopid": 28367850,
        "comment": "Mantap, tidak ada dent sama sekali, kondusi 95% kek baru, admin juga ramah pengiriman cepat, 3 hari sampe kalimantan. Mudah\"an awet",
        "rating_star": 5,
        "author_username": "srimagfirah"
    }, {
        "itemid": 24407157243,
        "ctime": 1726486382,
        "userid": 208844875,
        "shopid": 1021187906,
        "comment": "Fungsi:alhamdulillaah baik\nKondisi Barang:like new\nSpesifikasi:8/256 macbook pro 2016\n\nBarang rekomendasi, sudah di tes fitur dan lain lain okeee, kuliatas bersaing banget 🔥🔥🚀🚀🚀\n\nSemoga aweeet gada kendala, berkah selalu ✊✊✊",
        "rating_star": 5,
        "author_username": "azaam.13"
    }, {
        "itemid": 24407157243,
        "ctime": 1729168606,
        "userid": 18698153,
        "shopid": 1021187906,
        "comment": "Fungsi:gile mulus bgt dpt harga sale semoga awet",
        "rating_star": 5,
        "author_username": "prismshop"
    }, {
        "itemid": 24407157243,
        "ctime": 1727527123,
        "userid": 80869471,
        "shopid": 1021187906,
        "comment": "mantul.. muluz.. like new.. smuanya fungsi normal.. CS nya ramah & fast respon, konsultasi produk, request video produk via chat dilayani dengan baik.. recommended blanja dimari.. terima kasih..",
        "rating_star": 5,
        "author_username": "a*****u"
    }, {
        "itemid": 25415760327,
        "ctime": 1730313050,
        "userid": 126588345,
        "shopid": 28367850,
        "comment": "Kondisi:mulus\nFungsi:normal 100%\nSpesifikasi:sesuai deskripsi\n\nSeller Ramah , tanya2 selalu di respon. barang nyampe selamat karena pakingnya juga aman. ga ada komplaiin tentang barang. pokoknya top.\n\nyg jadi ganjal itu bonus tas nya. tidak serius. semoga diperbaiki ke depannya. \n\nsemoga laptop nya awet dipake kerja, dan seller rezekinya lancar.\nAamiin.",
        "rating_star": 5,
        "author_username": "giantfellaz_official"
    }, {
        "itemid": 25415760327,
        "ctime": 1722501069,
        "userid": 1253810369,
        "shopid": 28367850,
        "comment": "Fungsi:bagus\nKondisi Barang:bagus\n\nLaptop masih mulus \nsesuai deskripsi 🙏",
        "rating_star": 5,
        "author_username": "q*****4"
    }, {
        "itemid": 25415760327,
        "ctime": 1728377781,
        "userid": 56707895,
        "shopid": 28367850,
        "comment": "Kondisi:mulus\nFungsi:mantap\nSpesifikasi:sesuai\n\nSemoga awet. Seller recommended",
        "rating_star": 5,
        "author_username": "kamer_sumarorong"
    }, {
        "itemid": 25415760327,
        "ctime": 1732619346,
        "userid": 9577367,
        "shopid": 28367850,
        "comment": "Kondisi:baik\nFungsi:ok\nSpesifikasi:sesuai\n\nWalau agak lama kirimnya. Ngk nyangka sebagus ini.. Suaranya/🔊 ok. layarnya ok. casnya ok.slide barunya ok juga. Pokonya puas dah. Awalnya ragu. Tapi ternyata seleranya amanah. Mantap",
        "rating_star": 4,
        "author_username": "lorifebriady"
    }, {
        "itemid": 25415760327,
        "ctime": 1734327048,
        "userid": 142105653,
        "shopid": 28367850,
        "comment": "Fungsi:berfungsi baik semua\nKondisi:aman semua,jos\nSpesifikasi:macbook pro 2019",
        "rating_star": 5,
        "author_username": "bilalal.rabbah95"
    }]
