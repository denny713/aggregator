# Data Aggregator & Preprocessing Tool

## Deskripsi Project
Aplikasi web canggih dan terintegrasi untuk mengumpulkan (scraping) data secara otomatis dan memproses teks dari berbagai sumber digital seperti media sosial, marketplace e-commerce, publikasi akademik, platform berita, dan layanan web lainnya. Project ini dibangun menggunakan **Flask** sebagai backend yang robust dan stabil, serta kombinasi **HTML, JavaScript, jQuery, Bootstrap, dan CSS** untuk frontend yang responsif dan user-friendly. 

Aplikasi ini sangat berguna untuk penelitian akademik, analisis sentimen, riset pasar, dan berbagai keperluan data science yang memerlukan pengumpulan data dalam skala besar dengan preprocessing yang konsisten dan berkualitas.

## 🚀 Fitur Utama

### 1. Data Scraping
Aplikasi ini dapat mengumpulkan data dari 20+ sumber berbeda yang terbagi dalam beberapa kategori:

#### Media Sosial
- **Facebook** - Scraping konten postingan, komentar, dan interaksi pengguna
- **Instagram** - Mengumpulkan data dari postingan, caption, hashtag, dan engagement metrics
- **YouTube** - Data video lengkap termasuk judul, deskripsi, komentar, views, dan metadata
- **Twitter** - Tweet, retweet, mention, hashtag trending, dan analisis sentiment real-time
- **TikTok** - Konten video viral, caption, soundtrack, dan statistik engagement

#### Platform Marketplace & E-commerce
- **Play Store** (Indonesia & Internasional) - Data aplikasi lengkap, review pengguna, rating, download count, dan analisis trend aplikasi
- **App Store** (Indonesia & Internasional) - Informasi aplikasi iOS, metadata developer, pricing, dan user feedback
- **Tokopedia** - Produk detail, review customer, rating penjual, harga historis, dan analisis kompetitor
- **Shopee** - Data e-commerce komprehensif, flash sale, voucher, seller performance, dan trend produk
- **Bukalapak** - Informasi marketplace lokal, katalog produk, review pembeli, dan analisis UMKM Indonesia

#### Publikasi Akademik & Literatur
- **IEEE Xplore** - Paper dan jurnal ilmiah
- **ACM Digital Library** - Publikasi komputer science
- **Springer** - Jurnal dan buku akademik
- **Google Scholar** - Penelitian dan sitasi akademik
- **Science Direct** - Database jurnal Elsevier
- **Book Online** - Data buku digital
- **Wikipedia** (Indonesia & Inggris) - Artikel ensiklopedia

#### Platform Q&A dan Berita
- **Stack Overflow** - Pertanyaan dan jawaban programming
- **Detik** - Berita dan artikel Indonesia

### 2. Text Preprocessing
Aplikasi menyediakan berbagai teknik preprocessing text yang komprehensif

#### Pembersihan Data
- **Remove Username** - Menghilangkan mention username (@user)
- **Remove Retweet** - Menghapus indikator RT (Retweet)
- **Remove Hashtag** - Menghilangkan hashtag (#tag)
- **Remove URL** - Menghapus link dan URL
- **Remove Punctuation** - Menghilangkan tanda baca
- **Remove Symbol** - Menghapus simbol khusus
- **Remove Number** - Menghilangkan angka
- **Remove Duplicate** - Menghapus data duplikat

#### Normalisasi Text & Standarisasi
- **Replace Slang** - Mengganti kata slang dengan kata baku menggunakan dataset komprehensif bahasa Indonesia gaul dan media sosial
- **Replace Abbreviation** - Mengubah singkatan dan akronim menjadi kata penuh berdasarkan kamus standar
- **Replace Elongated Characters** - Memperbaiki karakter yang diperpanjang secara otomatis (contoh: "bagusssss" → "bagus", "cantiiikk" → "cantik")
- **Lower Case** - Transformasi konsisten semua text menjadi huruf kecil untuk standardisasi input
- **Text Normalization** - Proses normalisasi otomatis untuk konsistensi format data

#### Text Processing Lanjutan
- **Remove Stopwords** - Menghilangkan kata-kata tidak penting (bahasa Indonesia)
- **Stemming** - Mengubah kata menjadi bentuk dasar menggunakan Sastrawi
- **Tokenizing** - Memecah text menjadi token/kata individual
- **Join Case** - Menggabungkan kata tanpa spasi

### 3. Export Data & Analytics
- **Download CSV** - Ekspor hasil preprocessing dalam format CSV terstruktur dan siap analisis
- **Real-time Preview** - Melihat hasil preprocessing secara langsung dengan interface yang intuitif
- **Batch Processing** - Pemrosesan data dalam jumlah besar secara efisien
- **Quality Metrics** - Statistik kualitas data dan tingkat keberhasilan preprocessing

## 🌟 Keunggulan Aplikasi

- **Multi-Platform Integration** - Satu aplikasi untuk 20+ sumber data berbeda
- **Advanced Text Processing** - Preprocessing khusus untuk bahasa Indonesia dengan akurasi tinggi
- **Scalable Architecture** - Dapat menangani volume data besar dengan performa optimal
- **User-Friendly Interface** - Desain responsif dan mudah digunakan untuk semua level pengguna
- **Real-time Processing** - Pemrosesan data secara real-time dengan feedback langsung
- **Customizable Workflow** - Fleksibilitas dalam memilih dan mengkombinasikan teknik preprocessing
- **Research-Ready Output** - Format output yang langsung siap untuk analisis akademik dan industri

## 🛠️ Teknologi yang Digunakan

### Backend
- **Flask** - Framework web Python
- **Sastrawi** - Library stemming bahasa Indonesia
- **NLTK** - Natural Language Toolkit untuk preprocessing
- **Pandas** - Manipulasi dan analisis data
- **Beautiful Soup** - Web scraping
- **Selenium** - Web automation untuk scraping dinamis
- **Requests** - HTTP requests untuk API calls

### Frontend
- **HTML5** - Struktur web
- **CSS3** - Styling dan layout
- **JavaScript** - Interaktivitas web
- **jQuery** - DOM manipulation dan AJAX
- **Bootstrap 5** - Framework CSS responsive
- **Font Awesome** - Icon library
- **DataTables** - Table enhancement
- **SweetAlert2** - Modal dan notifikasi

### Libraries Scraping
- **Selenium** - Browser automation
- **Beautiful Soup** - HTML parsing
- **Requests-HTML** - HTTP requests dengan JavaScript support
- **Google Play Scraper** - Play Store API
- **App Store Scraper** - iOS App Store API
- **Wikipedia** - Wikipedia API
- **Instagrapi** - Instagram API

## 💻 System Requirements

- **Python 3.8+** (Direkomendasikan Python 3.9 atau lebih tinggi)
- **RAM minimum 4GB** (8GB untuk performa optimal)
- **Storage kosong 2GB** untuk dependencies dan cache data
- **Koneksi internet stabil** untuk proses scraping
- **Browser modern** (Chrome, Firefox, Safari, Edge)

## 📦 Instalasi

1. **Clone repository**
```bash
git clone https://github.com/denny713/aggregator.git
cd aggregator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download NLTK data**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

4. **Jalankan aplikasi**
```bash
python app.py
```

5. **Akses aplikasi**
Buka browser dan akses `http://localhost:7878`

## 🖥️ Cara Penggunaan

1. **Pilih Sumber Data**
   - Gunakan sidebar untuk memilih kategori (Social Media, Marketplace, Academic, dll.)
   - Klik platform yang ingin di-scrape

2. **Konfigurasi Scraping**
   - Masukkan kata kunci pencarian
   - Tentukan jumlah data yang ingin dikumpulkan
   - Pilih tipe data (jika diperlukan)

3. **Preprocessing Data**
   - Pilih teknik preprocessing yang diinginkan
   - Aplikasikan multiple preprocessing sekaligus
   - Preview hasil preprocessing

4. **Export Hasil**
   - Download data hasil preprocessing dalam format CSV
   - Data siap untuk analisis lebih lanjut

## 📁 Struktur Project

```
aggregator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── pages/
│   └── index.html        # Frontend interface
├── assets/
│   ├── css/
│   │   └── style.css     # Custom styling
│   ├── js/
│   │   ├── prepro.js     # Preprocessing logic
│   │   ├── process.js    # Data processing
│   │   └── util.js       # Utility functions
│   └── csv/              # Dataset files
│       ├── slang_dataset.csv
│       ├── abbre_dataset.csv
│       ├── elochar_dataset.csv
│       └── punctuation.csv
└── scrape/               # Scraping modules
    ├── facebook.py
    ├── instagram.py
    ├── youtube.py
    └── [18+ other scrapers]
```

## 🔧 Konfigurasi

Aplikasi berjalan pada port **7878** secara default. Untuk mengubah konfigurasi:

1. Edit file `app.py`
2. Ubah parameter pada `app.run(debug=True, port=7878)`
3. Sesuaikan pengaturan database atau API keys jika diperlukan

## 📝 Dataset Preprocessing

Aplikasi menggunakan beberapa dataset untuk preprocessing:
- **slang_dataset.csv** - Kamus kata slang ke kata baku
- **abbre_dataset.csv** - Kamus singkatan dan kepanjangan
- **elochar_dataset.csv** - Daftar kata dengan karakter berulang
- **punctuation.csv** - Daftar tanda baca

## ⚠️ Catatan Penting & Best Practices

### Penggunaan Etis
- Pastikan koneksi internet stabil untuk proses scraping yang optimal
- Beberapa platform memiliki rate limiting, gunakan dengan bijak dan tidak berlebihan
- Scraping harus mematuhi robots.txt dan terms of service setiap platform
- Data yang dikumpulkan hanya untuk tujuan penelitian, edukasi, dan analisis non-komersial
- Hormati privasi pengguna dan jangan scraping data personal yang sensitif

### Tips Performa
- Gunakan batch size yang sesuai untuk menghindari timeout
- Lakukan scraping pada jam dengan traffic rendah untuk hasil optimal
- Simpan data secara berkala untuk menghindari kehilangan data
- Monitor penggunaan memori saat memproses dataset besar

### Troubleshooting Umum
- **Error koneksi**: Periksa firewall dan proxy settings
- **Data kosong**: Cek kata kunci pencarian dan ketersediaan data di platform
- **Proses lambat**: Kurangi ukuran batch atau upgrade spesifikasi sistem
- **Memory error**: Proses data dalam chunk yang lebih kecil

## ❓ FAQ (Frequently Asked Questions)

**Q: Apakah aplikasi ini gratis untuk digunakan?**
A: Ya, aplikasi ini open source dan gratis untuk tujuan penelitian dan edukasi.

**Q: Berapa maksimal data yang bisa di-scrape dalam sekali proses?**
A: Tergantung platform dan spesifikasi sistem, umumnya 1000-5000 data per batch untuk performa optimal.

**Q: Apakah data yang di-scrape disimpan secara permanen?**
A: Tidak, data hanya tersimpan sementara di session browser dan dapat di-download sebagai CSV.

**Q: Bisakah menambahkan platform scraping baru?**
A: Ya, Anda bisa kontribusi dengan menambahkan modul scraper baru di folder `/scrape/`.

## 🚀 Roadmap Pengembangan

### Version 2.0 (Planning)
- [ ] Support untuk format export JSON dan Excel
- [ ] Integrasi dengan database (MongoDB, PostgreSQL)
- [ ] API endpoints untuk integrasi eksternal
- [ ] Dashboard analytics dan visualisasi data
- [ ] Machine learning untuk klasifikasi otomatis
- [ ] Multi-language support (English interface)
- [ ] Scheduled scraping dan automation

### Version 2.1 (Future)
- [ ] Cloud deployment options (Docker, AWS)
- [ ] Real-time streaming data processing
- [ ] Advanced sentiment analysis
- [ ] Custom preprocessing rules
- [ ] Collaborative workspace features

## 🤝 Kontribusi

Kontribusi dan feedback sangat diterima! Silakan:
1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/amazing-feature`)
3. Commit perubahan Anda (`git commit -m 'Add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buat Pull Request dengan deskripsi detail

### Cara Berkontribusi
- **Bug Reports**: Laporkan bug melalui GitHub Issues
- **Feature Requests**: Suggest fitur baru yang dibutuhkan
- **Code Contributions**: Perbaikan kode, optimisasi, atau fitur baru
- **Documentation**: Perbaikan dokumentasi dan tutorial
- **Testing**: Bantuan testing di berbagai environment

## 📄 Lisensi

Project ini dibuat untuk tujuan edukasi dan penelitian. Pastikan mematuhi ketentuan penggunaan setiap platform yang di-scrape.

## 🙏 Acknowledgments

- **Sastrawi Library** - Untuk stemming bahasa Indonesia yang powerful
- **NLTK Team** - Untuk natural language processing tools yang comprehensive
- **Flask Community** - Untuk framework web yang simple dan elegant
- **Bootstrap Team** - Untuk UI framework yang responsive dan modern
- **Open Source Community** - Untuk semua library dan tools yang memungkinkan project ini ada

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/denny713/aggregator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/denny713/aggregator/discussions)
- **Email**: Untuk pertanyaan akademik dan kolaborasi
- **Documentation**: Lengkap tersedia di repository ini

## 📈 Stats & Usage

![GitHub Stars](https://img.shields.io/github/stars/denny713/aggregator?style=social)
![GitHub Forks](https://img.shields.io/github/forks/denny713/aggregator?style=social)
![GitHub Issues](https://img.shields.io/github/issues/denny713/aggregator)
![GitHub License](https://img.shields.io/github/license/denny713/aggregator)

---
**Dikembangkan dengan ❤️ untuk memudahkan penelitian dan analisis data digital Indonesia**

*"Memberdayakan peneliti, akademisi, dan data scientist Indonesia dengan tools yang powerful dan mudah digunakan"*