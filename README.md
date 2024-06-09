# Web Crawler dengan Python

## Deskripsi

Proyek ini adalah implementasi web crawler yang menggunakan bahasa pemrograman Python. Web Crawler ini mengekstrak data dari situs web secara otomatis dengan mengunjungi halaman-halaman yang berbeda. Crawler akan menyimpan informasi yang diperoleh seperti judul halaman, tautan, dan konten dalam bentuk terstruktur.

## Fitur Utama

1. **Ekstraksi Data Halaman:** Mengambil judul, tautan, dan konten dari halaman web.
2. **Pengindeksan Tautan:** Mengidentifikasi dan mengikuti tautan internal untuk mengindeks lebih banyak halaman.
3. **Pemfilteran Tautan:** Menghindari tautan duplikat dan mengindeks hanya tautan yang relevan.
4. **Kepatuhan `robots.txt`:** Memastikan crawler menghormati aturan `robots.txt` dari situs web.
5. **Penanganan Batasan Server:** Menambahkan jeda antara permintaan untuk menghindari pemblokiran oleh server web.
6. **Penyimpanan Data:** Menyimpan data yang diekstrak ke dalam format yang terstruktur seperti CSV atau database.

## Struktur Proyek
```
web-crawler/
│
├── src/
│ ├── crawler.py
│ ├── parser.py
│ ├── storage.py
│ └── utils.py
├── tests/
│ ├── test_crawler.py
│ ├── test_parser.py
│ ├── test_storage.py
│ └── test_utils.py
├── requirements.txt
└── README.md
```
## Cara Penggunaan

### Instalasi

1. Clone repositori ini ke lokal Anda:

   ```bash
   git clone https://github.com/imhunterand/web-crawler.git
   cd web-crawler
   pip install -r requirements.txt
   python src/crawler.py
   python -m unittest discover tests
   ```

## Cara Kerja
Crawler akan memulai dengan URL yang diberikan, mengunduh halaman tersebut, dan mengekstrak tautan, judul, dan konten. Selanjutnya, crawler akan mengikuti tautan internal untuk mengindeks lebih banyak halaman, dengan mematuhi aturan robots.txt dan menghindari pemblokiran oleh server web dengan menambahkan jeda antara permintaan.

## Penyimpanan Data
Data yang diekstrak akan disimpan dalam format CSV secara default. Anda juga bisa mengubah kode untuk menyimpan data ke dalam database SQLite dengan mengubah fungsi penyimpanan di `src/storage.py`.

### Kontak Support
Jika Anda memiliki pertanyaan atau masukan, silakan hubungi saya di imhunterand@andri.dev
