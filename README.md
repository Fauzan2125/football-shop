Aplikasi Football Shop - Moy's Football Store

https://ahmad-fauzan45-footballshop.pbp.cs.ui.id

A. - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -

1. Membuat Proyek Django Baru
- Saya membuat direktori baru `football-shop-app`
- Membuat virtual environment dengan `python -m venv env`
- Mengaktifkan virtual environment dan menginstall Django
- Membuat proyek Django dengan nama `football_shop`

2. Membuat Aplikasi Main
- Menjalankan `python manage.py startapp main`
- Mendaftarkan aplikasi `main` di `INSTALLED_APPS` dalam `settings.py`

3. Melakukan Routing pada Proyek
- Membuat file `urls.py` di dalam aplikasi `main`
- Mengkonfigurasi URL patterns untuk mengarahkan ke fungsi view
- Menghubungkan URL aplikasi main dengan URL proyek utama

4. Membuat Model Product
- Membuat model `Product` di `main/models.py` dengan atribut wajib:
  - `name` (CharField): nama produk
  - `price` (IntegerField): harga produk
  - `description` (TextField): deskripsi produk
  - `thumbnail` (URLField): gambar produk
  - `category` (CharField): kategori produk
  - `is_featured` (BooleanField): status produk unggulan
- Menambahkan atribut tambahan seperti `stock`, `brand`, dan `rating`

5. Membuat Fungsi View
- Membuat fungsi `show_main` di `views.py` yang mengembalikan render template
- Mengirim data context berisi nama aplikasi, nama mahasiswa, kelas, dan data produk

6. Membuat Template HTML
- Membuat direktori `templates` di dalam aplikasi main
- Membuat file `main.html` dengan desain yang menarik menggunakan CSS
- Menampilkan informasi yang diminta dan daftar produk

7. Deployment ke PWS
- Menyiapkan file requirements.txt
- Mengkonfigurasi settings untuk production
- Melakukan deployment ke PWS sesuai panduan

B. - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html. -
[Client] --> [URLs.py] --> [Views.py] --> [Models.py] --> [Database]
^                           |                            |
|                           v                            v
[Response] <-- [HTML Template] <-- [Context Data] <-- [Query Results]

Penjelasan Alur:
1. Client mengirim HTTP request ke server Django
2. `urls.py` menerima request dan mencocokkan pola URL dengan fungsi view yang sesuai
3. `views.py` memproses request, berinteraksi dengan `models.py` jika perlu data dari database
4. `models.py` melakukan query ke database dan mengembalikan hasilnya
5. `views.py` menyiapkan context data dan merender template HTML
6. Template HTML digabungkan dengan context data untuk menghasilkan response
7. Response HTML dikirim kembali ke client

C. - Jelaskan peran `settings.py` dalam proyek Django! -

`settings.py` adalah file konfigurasi utama dalam proyek Django yang berperan sebagai pusat pengaturan untuk seluruh aplikasi. Beberapa peran penting:
1. Konfigurasi Database: Menentukan jenis database, nama database, dan kredensial akses
2. Pengaturan Aplikasi: Mendaftarkan aplikasi yang akan digunakan dalam proyek melalui `INSTALLED_APPS`
3. Middleware Configuration: Mengatur middleware yang akan dijalankan pada setiap request/response
4. Template Settings: Konfigurasi lokasi dan engine template yang digunakan
5. Static Files: Pengaturan untuk file statis seperti CSS, JavaScript, dan gambar
6. Security Settings: Konfigurasi keamanan seperti `SECRET_KEY`, `ALLOWED_HOSTS`, dll.
7. Timezone & Localization: Pengaturan zona waktu dan lokalisasi aplikasi

D. - Bagaimana cara kerja migrasi database di Django? -

Migrasi database di Django bekerja melalui sistem yang terstruktur:
1. Deteksi Perubahan: Django mendeteksi perubahan pada model melalui perintah `makemigrations`
2. Pembuatan File Migrasi: Django membuat file Python yang berisi instruksi perubahan skema database
3. Penerapan Migrasi: Perintah `migrate` menjalankan file migrasi dan mengubah struktur database
4. Tracking: Django mencatat migrasi yang sudah dijalankan di tabel `django_migrations`
5. Reversibility: Migrasi dapat di-rollback jika diperlukan

Keuntungan sistem migrasi:
- Version control untuk skema database
- Sinkronisasi database antar tim developer
- Deployment yang konsisten
- Rollback yang aman

E. - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? -

Django menjadi pilihan ideal untuk pembelajaran karena:
1. Batteries Included: Django menyediakan banyak fitur built-in (ORM, admin panel, authentication)
2. Struktur yang Jelas: Pola MVT memberikan struktur yang mudah dipahami
3. Dokumentasi Lengkap: Django memiliki dokumentasi yang sangat komprehensif
4. Komunitas Besar: Dukungan komunitas yang kuat dengan banyak tutorial dan resources
5. Rapid Development: Memungkinkan pengembangan aplikasi web dengan cepat
6. Security by Default: Django menerapkan best practices keamanan secara default
7. Scalable: Dapat digunakan untuk aplikasi kecil hingga enterprise
8. Python-based: Menggunakan Python yang mudah dipelajari dan dibaca
9. Convention over Configuration: Mengurangi kompleksitas konfigurasi

F. - Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? -
- Tutorial sudah jelas dan mudah diikuti
- Penjelasan konsep MVT sangat membantu pemahaman
- Apresiasi untuk respon asdos yang cepat dalam menjawab pertanyaan