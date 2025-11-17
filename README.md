# Data Aggregator & Preprocessing Tool

## Deskripsi Project
Aplikasi web untuk mengumpulkan (scraping) dan memproses data dari berbagai sumber digital seperti media sosial, marketplace, publikasi akademik, dan platform lainnya. Project ini dibangun menggunakan **Flask** sebagai backend dan kombinasi **HTML, JavaScript, jQuery, Bootstrap, dan CSS** untuk frontend.

## 🚀 Fitur Utama

### 1. Data Scraping
Aplikasi ini dapat mengumpulkan data dari 20+ sumber berbeda yang terbagi dalam beberapa kategori:

#### Media Sosial
- **Facebook** - Scraping konten dan postingan
- **Instagram** - Mengumpulkan data dari postingan
- **YouTube** - Data video dan komentar
- **Twitter** - Tweet dan data sosial media
- **TikTok** - Konten video dan metadata

#### Platform Marketplace
- **Play Store** (Indonesia & Internasional) - Data aplikasi dan review
- **App Store** (Indonesia & Internasional) - Informasi aplikasi iOS
- **Tokopedia** - Produk dan review marketplace Indonesia
- **Shopee** - Data e-commerce dan produk
- **Bukalapak** - Informasi marketplace lokal

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
Aplikasi menyediakan berbagai teknik preprocessing text yang komprehensif:

#### Pembersihan Data
- **Remove Username** - Menghilangkan mention username (@user)
- **Remove Retweet** - Menghapus indikator RT (Retweet)
- **Remove Hashtag** - Menghilangkan hashtag (#tag)
- **Remove URL** - Menghapus link dan URL
- **Remove Punctuation** - Menghilangkan tanda baca
- **Remove Symbol** - Menghapus simbol khusus
- **Remove Number** - Menghilangkan angka
- **Remove Duplicate** - Menghapus data duplikat

#### Normalisasi Text
- **Replace Slang** - Mengganti kata slang dengan kata baku (menggunakan dataset slang)
- **Replace Abbreviation** - Mengubah singkatan menjadi kata penuh
- **Replace Elongated Characters** - Memperbaiki karakter yang diperpanjang (contoh: "bagusssss" → "bagus")
- **Lower Case** - Mengubah semua text menjadi huruf kecil

#### Text Processing Lanjutan
- **Remove Stopwords** - Menghilangkan kata-kata tidak penting (bahasa Indonesia)
- **Stemming** - Mengubah kata menjadi bentuk dasar menggunakan Sastrawi
- **Tokenizing** - Memecah text menjadi token/kata individual
- **Join Case** - Menggabungkan kata tanpa spasi

### 3. Export Data
- **Download CSV** - Ekspor hasil preprocessing dalam format CSV
- **Real-time Preview** - Melihat hasil preprocessing secara langsung

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

## ⚠️ Catatan Penting

- Pastikan koneksi internet stabil untuk proses scraping
- Beberapa platform memiliki rate limiting, gunakan dengan bijak
- Scraping harus mematuhi robots.txt dan terms of service platform
- Data yang dikumpulkan hanya untuk tujuan penelitian dan edukasi

## 🤝 Kontribusi

Kontribusi selalu diterima! Silakan:
1. Fork repository
2. Buat feature branch
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

## 📄 Lisensi

Project ini dibuat untuk tujuan edukasi dan penelitian. Pastikan mematuhi ketentuan penggunaan setiap platform yang di-scrape.

---
**Dibuat dengan ❤️ untuk memudahkan penelitian dan analisis data digital**