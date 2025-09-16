Aplikasi Football Shop - Moy's Football Store

https://ahmad-fauzan45-footballshop.pbp.cs.ui.id

TUGAS 2

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

TUGAS 3

A. - Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? -
Bayangkan platform digital itu seperti restoran. Dapur (backend) adalah tempat semua makanan (data) diolah, sementara meja makan (frontend) adalah tempat pelanggan (pengguna) menikmatinya. Nah, data delivery adalah pelayan yang bolak-balik mengantar pesanan dari meja ke dapur dan mengantar makanan dari dapur ke meja. Tanpa "pelayan" ini, aplikasi di HP kita nggak akan pernah bisa berkomunikasi dengan server untuk memesan ojek, melihat status pesanan, atau membayar tagihan. Jadi, data delivery adalah penghubung vital yang membuat seluruh bagian platform bisa "ngobrol" dan bekerja sama, baik di dalam aplikasi itu sendiri maupun dengan layanan pihak ketiga (seperti sistem pembayaran).

B. - Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? -
Untuk sebagian besar kebutuhan web modern, JSON jelas lebih unggul. Anggap saja JSON itu seperti catatan ringkas dalam format poin-poin yang rapi, sementara XML itu seperti dokumen resmi dengan banyak aturan format yang kaku. JSON lebih ringan, lebih cepat dibaca oleh mesin (terutama oleh JavaScript di browser), dan lebih gampang dimengerti manusia. Popularitasnya meroket karena kesederhanaan dan efisiensinya ini, apalagi mayoritas API (jembatan komunikasi antar aplikasi) saat ini menggunakan JSON sebagai bahasa standarnya. XML masih punya tempatnya di sistem yang kompleks dan butuh struktur dokumen yang ketat, tapi untuk pertukaran data sehari-hari di web, JSON adalah juaranya.

C. - Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? -
Method is_valid() pada dasarnya adalah satpam super teliti untuk setiap data yang dikirim pengguna lewat form. Sebelum data itu diizinkan masuk dan diolah (misalnya, disimpan ke database), is_valid() akan memeriksa semuanya. Apakah email diisi dengan format yang benar? Apakah umur diisi dengan angka, bukan huruf? Apakah password memenuhi syarat panjang minimal? Jika semua aturan terpenuhi, ia akan memberi cap "aman" (True) dan menyajikan data yang sudah bersih di cleaned_data. Jika ada satu saja yang melanggar, ia akan menolak data itu (False) dan mencatat semua kesalahannya agar bisa kita tampilkan ke pengguna. Tanpa "satpam" ini, kita harus memeriksa data secara manual, yang sangat merepotkan dan berbahaya.

D. - Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? -
Kita butuh csrf_token untuk mencegah serangan Cross-Site Request Forgery (CSRF). Bayangkan kita lagi login di aplikasi bank, lalu tanpa sadar kita mengklik link di email iseng. Ternyata, link itu diam-diam mengirim perintah dari komputer kita ke aplikasi bank untuk mentransfer uang. Karena aplikasi bank melihat permintaan itu datang dari browser kita yang sudah login, permintaan itu dianggap sah. Nah, csrf_token mencegah ini dengan cara memberikan "tiket rahasia" unik di dalam form di situs asli. Ketika kita mengirim form, Django akan mencocokkan tiket di form dengan tiket yang disimpannya. Situs penipu nggak akan punya tiket rahasia ini, jadi ketika mereka mencoba mengirim perintah palsu atas nama kita, permintaannya akan langsung ditolak karena "nggak punya tiket masuk". Jika kita tidak pakai csrf_token, akun pengguna bisa dibajak untuk melakukan aksi apa pun (ganti password, hapus data, kirim uang) tanpa mereka sadari.

E. - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -
- Langkah 1: Membuat Cetak Biru Produk (Model & Form) 
Langkah pertama adalah mendefinisikan informasi apa saja yang kita perlukan untuk setiap produk. Untuk Football Shop, kita mungkin butuh nama produk (misalnya, "Jersey Kandang Real Madrid 2025/26"), nama klub, harga, dan jumlah stok. Ini adalah "cetak biru" atau blueprint data kita. Berdasarkan cetak biru ini, kita kemudian meminta Django untuk secara otomatis membuatkan sebuah formulir web yang berisi kolom-kolom isian yang sesuai, jadi kita tidak perlu membuatnya satu per satu secara manual.

- Langkah 2: Merakit Otak Logika (Views) 
Selanjutnya, kita membangun "otak" di balik layar yang akan mengelola formulir tersebut. Logika ini punya dua tugas utama. Pertama, ketika kita membuka halaman "Tambah Produk", ia akan menampilkan formulir yang masih kosong. Kedua, ketika kita mengisi formulir dan menekan tombol "Simpan", logika ini akan menangkap semua data yang kita kirim, menjalankan pemeriksaan keamanan dan validasi melalui method is_valid() untuk memastikan datanya benar dan aman. Jika semuanya lolos, data produk baru tersebut akan disimpan ke database toko kita.

- Langkah 3: Membangun Etalase Toko (Template) 
Di sini, kita mendesain halaman web yang akan dilihat oleh pengguna. Kita membuat sebuah formulir HTML dan, yang paling penting, menyisipkan csrf_token di dalamnya sebagai "kunci pengaman" wajib untuk mencegah serangan dari luar. Setelah itu, kita tinggal memerintahkan Django untuk menampilkan semua kolom isian yang sudah kita definisikan di langkah pertama, lengkap dengan sebuah tombol "Simpan Produk".

- Langkah 4: Mengirim Info Produk ke Sistem Lain (Data Delivery) 
Ini adalah bagian di mana konsep data delivery menjadi nyata. Setelah sebuah jersey baru berhasil disimpan di database kita, anggap kita perlu memberitahu sistem lain, misalnya sistem gudang pusat atau marketplace partner. Di sinilah JSON dan XML berperan sebagai "bahasa pengiriman".

- Langkah 5: Cara Modern dengan JSON (Paling Umum)
Kita bisa membayangkan JSON seperti mengirim pesan singkat atau catatan ringkas yang sangat terstruktur. Kita ambil detail produk baru (nama, harga, stok), lalu kita susun dalam format poin-poin yang sederhana. "Catatan digital" ini kemudian kita kirim lewat internet ke sistem partner. Karena JSON adalah bahasa standar untuk sebagian besar API modern, sistem partner akan langsung mengerti pesan kita dengan mudah dan cepat.

Cara Klasik dengan XML (Untuk Sistem Lama)
Jika partner kita menggunakan sistem yang lebih tua, mereka mungkin tidak bisa membaca "pesan singkat" dan malah membutuhkan sebuah dokumen resmi. Di sinilah XML digunakan. Kita mengambil detail produk yang sama, tetapi kali ini kita membungkus setiap informasi dengan "label" atau tag yang deskriptif. Hasilnya adalah sebuah "dokumen digital" yang lebih formal dan kaku. Meskipun lebih 'bertele-tele' daripada JSON, cara ini memastikan sistem lama milik partner bisa membaca dan memahami data yang kita kirim dengan benar.

F. - Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan? -
- Tutorial sudah jelas dan mudah diikuti
- Penjelasan Form dan Data Delivery sangat membantu pemahaman
- Apresiasi untuk respon asdos yang cepat dalam menjawab pertanyaan

Link Screenshoot Postman:
https://drive.google.com/drive/folders/1Bh7MzWwoqIGo3-CqQlO00IzbBvTO0A2w?usp=sharing




 