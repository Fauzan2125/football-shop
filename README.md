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

TUGAS 4

A. - Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya. -
Django AuthenticationForm adalah sebuah form bawaan dari Django yang secara khusus dirancang untuk menangani proses login pengguna. Form ini sudah jadi dan siap pakai, isinya ada dua field utama: username dan password.

Kelebihan:
- Cepat & Mudah: Kamu tidak perlu membuat form login dari nol. Cukup impor dan gunakan.
- Aman: Form ini sudah dilengkapi validasi keamanan dasar, seperti mengecek apakah username dan password yang dimasukkan cocok, dan memastikan akun pengguna tersebut aktif.
- Terintegrasi: Terhubung langsung dengan sistem autentikasi Django, sehingga proses validasi dan memasukkan user ke dalam session menjadi sangat mudah.

Kekurangan:
- Kurang Fleksibel: Secara default, form ini hanya menerima username dan password. Jika kamu ingin login menggunakan email sebagai gantinya, kamu perlu melakukan kustomisasi lebih lanjut.
- Tampilan Standar: Tampilannya sangat dasar, jadi kamu perlu menambahkan CSS sendiri agar terlihat bagus dan menyatu dengan desain web-mu.\

B. - Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut? -
Meskipun sering disebut bersamaan, keduanya adalah konsep yang berbeda.

1. Autentikasi (Authentication): "Kamu siapa?"
Ini adalah proses memverifikasi identitas seseorang. Saat kita memasukkan username dan password untuk login, sistem sedang melakukan autentikasi untuk memastikan kamu adalah benar-benar orang yang kamu klaim.
- Implementasi di Django: Django menanganinya lewat sistem django.contrib.auth. Fitur seperti login(), logout(), AuthenticationForm, dan model User adalah bagian dari sistem ini.

2. Otorisasi (Authorization) : "Kamu boleh ngapain aja?"
Ini adalah proses menentukan hak akses yang dimiliki oleh pengguna yang identitasnya sudah terverifikasi. Setelah kamu berhasil login (autentikasi), sistem akan mengecek apakah kamu punya izin untuk melakukan aksi tertentu, misalnya menghapus produk atau mengakses halaman admin.

- Implementasi di Django: Django menanganinya melalui sistem perizinan (permissions). Contohnya adalah dekorator @login_required yang hanya memberi izin akses halaman kepada pengguna yang sudah login, atau user.is_superuser yang mengecek apakah pengguna punya hak akses tertinggi.

C. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies dan session adalah dua cara untuk "mengingat" informasi pengguna saat mereka berpindah-pindah halaman di sebuah situs web.

1. Cookies 
Cara Kerja: Sepotong kecil data yang disimpan di browser pengguna. Setiap kali pengguna mengunjungi situs itu lagi, browser akan mengirimkan kembali cookie tersebut ke server.
Kelebihan:
- Persisten: Bisa diatur agar bertahan lama (berhari-hari atau bahkan berbulan-bulan), jadi bisa untuk mengingat login (remember me) atau preferensi tema.
- Beban Server Ringan: Karena data disimpan di sisi klien, tidak membebani penyimpanan di server.
Kekurangan:
- Tidak Aman untuk Data Sensitif: Karena disimpan di browser, isinya bisa dilihat dan dimanipulasi oleh pengguna. Sangat tidak disarankan menyimpan password atau data pribadi di sini.
- Ukuran Terbatas: Ukuran cookies sangat kecil (sekitar 4KB).

2. Session
Cara Kerja: Data disimpan di sisi server. Browser pengguna hanya menyimpan sebuah ID unik (session ID) di dalam cookie. Setiap kali pengguna membuat permintaan, session ID dikirim ke server, lalu server akan mencari data sesi yang sesuai dengan ID tersebut.
Kelebihan:
- Sangat Aman: Data sensitif (seperti siapa yang sedang login) disimpan di server, sehingga tidak bisa diakses atau diubah oleh pengguna.
- Ukuran Lebih Besar: Bisa menyimpan data yang jauh lebih besar dibandingkan cookies.
Kekurangan:
- Membebani Server: Setiap sesi pengguna akan memakan ruang di penyimpanan dan memori server.
- Bergantung pada Session ID: Jika session ID di cookie pengguna hilang atau kedaluwarsa, sesi akan berakhir.

D. - Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut? -
Tidak, cookies tidak aman secara default. Karena cookies disimpan di browser dalam bentuk teks biasa, ada beberapa risiko keamanan yang perlu diwaspadai:
- Cross-Site Scripting (XSS): Penyerang bisa menyisipkan skrip jahat di sebuah halaman web untuk mencuri data dari cookies pengguna.
- Cross-Site Request Forgery (CSRF): Penyerang bisa "memaksa" browser pengguna untuk melakukan tindakan yang tidak diinginkan (misalnya, transfer uang) di situs lain tempat pengguna sedang login, dengan memanfaatkan cookie sesi yang tersimpan.
- Session Hijacking: Jika seorang penyerang berhasil mendapatkan session ID milikmu (misalnya melalui jaringan Wi-Fi publik yang tidak aman), mereka bisa "membajak" sesimu dan menyamar sebagai dirimu.

Bagaimana Django Menanganinya?
Django memiliki beberapa lapisan keamanan bawaan untuk melindungi dari risiko-risiko ini:
- HttpOnly Cookies: Django secara default mengatur cookie sesi sebagai HttpOnly, yang berarti cookie tersebut tidak bisa diakses oleh JavaScript. Ini secara efektif mencegah pencurian cookie melalui serangan XSS.
- CSRF Token: Django secara otomatis menyertakan token CSRF di setiap form POST. Server akan memvalidasi token ini untuk memastikan bahwa permintaan tersebut benar-benar berasal dari situs web kita, bukan dari situs lain. Ini adalah perlindungan utama terhadap serangan CSRF.
- Secure Cookies: Django juga menyediakan opsi untuk mengatur cookies sebagai Secure, yang berarti cookie hanya akan dikirim melalui koneksi HTTPS yang terenkripsi, mencegah penyadapan di jaringan yang tidak aman.

E. - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -
1. Persiapan Awal: Pertama, saya membuat app baru bernama authentication untuk memisahkan logika terkait pengguna. Lalu, saya mengatur urls.py utama proyek agar menyertakan URL dari app baru ini.
2. Membuat Fungsi Login, Logout, Register:
- Register: Saya membuat fungsi register di views.py. Di dalamnya, saya menggunakan UserCreationForm bawaan Django untuk membuat form registrasi. Jika data valid, pengguna baru akan dibuat dan langsung di-login-kan.
- Login: Untuk fungsi login, saya menggunakan AuthenticationForm. Jika form valid, saya memanggil fungsi login() dari Django untuk memulai sesi pengguna dan menyimpan last_login ke dalam cookie.
- Logout: Ini yang paling simpel. Saya hanya perlu memanggil fungsi logout() dari Django untuk mengakhiri sesi.
3. Mengatur URL dan Template: Saya mendaftarkan path untuk ketiga fungsi di atas di authentication/urls.py. Kemudian, saya membuat tiga file HTML (login.html, register.html) dan memberikan styling dasar agar fungsional.
4. Menghubungkan Product dengan User: Di main/models.py, saya menambahkan ForeignKey ke model User di dalam model Product. Ini artinya, setiap produk sekarang "dimiliki" oleh seorang pengguna. Setelah mengubah model, saya menjalankan makemigrations dan migrate.
5. Menyesuaikan Logika Aplikasi:
- Di views.py aplikasi utama, saya menambahkan dekorator @login_required pada fungsi-fungsi yang hanya boleh diakses setelah login (seperti membuat produk).
- Saat membuat produk baru, saya mengatur agar product.user secara otomatis diisi dengan request.user.
- Di halaman utama, saya memfilter agar produk yang ditampilkan hanya produk milik pengguna yang sedang login. Saya juga menambahkan kode untuk menampilkan username dan last_login dari cookie.
6. Membuat Data Dummy: Terakhir, saya mendaftarkan 2 akun pengguna baru dan untuk masing-masing akun, saya membuat 3 data produk melalui aplikasi yang sudah berjalan untuk memenuhi syarat tugas.

TUGAS 5

A. - Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! -
 
Jika sebuah elemen HTML memiliki beberapa selector CSS, browser akan menentukan gaya mana yang akan diterapkan berdasarkan urutan prioritas yang disebut spesifisitas (specificity). Aturan dasarnya adalah, semakin spesifik sebuah selector, semakin tinggi prioritasnya.

Berikut adalah urutan prioritas dari yang tertinggi ke yang terendah:

1. Inline Styles: Atribut style yang ditulis langsung di dalam tag HTML. Ini adalah yang paling spesifik dan akan mengalahkan semua aturan lain.

Contoh: <p style="color: red;">Teks ini pasti merah.</p>

2. ID Selector: Selector yang menggunakan # untuk menargetkan ID unik sebuah elemen.

Contoh: #judul-utama { color: blue; }

3. Class, Attribute, dan Pseudo-class Selectors: Ini termasuk kelas (.nama-kelas), selector atribut ([type="text"]), dan pseudo-class (:hover, :focus).

Contoh: .tombol-submit { background-color: green; }

4. Element dan Pseudo-element Selectors: Ini adalah selector yang paling tidak spesifik, yang menargetkan semua tag dengan nama tertentu (p, div, h1) atau pseudo-element (::before, ::after).

Contoh: p { font-size: 16px; }

B. - Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa! -
Responsive Design adalah sebuah pendekatan dalam desain web yang membuat tampilan halaman web dapat beradaptasi secara otomatis dengan berbagai ukuran layar perangkat, mulai dari desktop besar hingga tablet dan smartphone.

Konsep ini menjadi sangat penting karena beberapa alasan utama:

1. Pengalaman Pengguna (User Experience): Mayoritas pengguna internet saat ini mengakses web melalui perangkat mobile. Desain yang responsif memastikan mereka mendapatkan pengalaman yang nyaman tanpa harus melakukan zoom atau menggeser layar secara horizontal.

2. Peningkatan Jangkauan Audiens: Dengan web yang berfungsi baik di semua perangkat, kita tidak akan kehilangan potensi pengunjung atau pelanggan yang menggunakan perangkat berbeda.

3. SEO (Search Engine Optimization): Mesin pencari seperti Google secara eksplisit memprioritaskan dan memberikan peringkat lebih tinggi untuk situs web yang mobile-friendly. Situs yang tidak responsif akan sulit ditemukan di hasil pencarian.

4. Efisiensi Pengembangan dan Perawatan: Daripada membuat beberapa versi situs web yang berbeda (satu untuk desktop, satu untuk mobile), kita hanya perlu mengelola satu basis kode yang fleksibel.

Contoh Aplikasi yang Sudah Menerapkan Responsive Design:

Tokopedia/Shopee: Jika kita membuka situs Tokopedia di desktop, Kita akan melihat layout dengan banyak kolom, sidebar, dan menu yang lebar. Namun, saat dibuka di smartphone, tampilannya berubah total menjadi satu kolom vertikal, gambar produk menjadi lebih besar, dan navigasi utama disembunyikan di dalam menu "hamburger" (ikon tiga garis). Ini dilakukan agar semua tombol mudah dijangkau oleh jari dan informasi tetap terbaca dengan jelas di layar kecil.

Contoh Aplikasi yang Belum Menerapkan Responsive Design:

SIAK NG adalah contoh sempurna dari aplikasi yang dirancang dengan pola pikir "desktop-first" dan hampir tidak mempertimbangkan pengguna mobile. Saat kita membukanya di HP, yang terjadi bukanlah adaptasi, melainkan seluruh halaman versi desktop "dikecilkan" agar muat di layar HP.

C.- Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! -
Ketiga properti ini adalah bagian fundamental dari CSS Box Model, yang mendefinisikan bagaimana elemen HTML dirender sebagai "kotak" di halaman.

1. Padding (Bantalan)

Definisi: Ruang transparan yang berada di dalam border, yaitu antara border dan konten utama elemen (teks/gambar).

Analogi: Seperti bantalan busa di dalam sebuah kotak. Busa tersebut (padding) melindungi isi kotak (konten) dari tepian kotak (border).

2. Border (Garis Tepi)

Definisi: Garis yang mengelilingi sebuah elemen, berada di antara padding dan margin.

Analogi: Seperti bingkai foto. Bingkai ini (border) memiliki ketebalan, warna, dan gaya (misalnya, garis lurus atau putus-putus).

3. Margin (Jarak)

Definisi: Ruang transparan yang berada di luar border. Fungsinya adalah untuk memberikan jarak antara elemen tersebut dengan elemen lain di sekitarnya.

Analogi: Seperti jarak antara satu bingkai foto dengan bingkai foto lainnya yang digantung di dinding.

Cara Implementasi di CSS:

.kotak-produk {
  // Memberi ruang 20px di dalam border 
  padding: 20px;
  
  // Membuat bingkai setebal 2px dengan gaya solid dan warna hitam 
  border: 2px solid black;
  
  // Memberi jarak 30px di luar border, mendorong elemen lain menjauh 
  margin: 30px; 
}

D. - Jelaskan konsep flex box dan grid layout beserta kegunaannya! -
Flexbox dan Grid adalah dua sistem layout modern di CSS yang dirancang untuk mempermudah pembuatan tata letak halaman yang kompleks dan responsif.

1. Flexbox (Flexible Box Layout)

Konsep: Sistem layout satu dimensi. Artinya, Flexbox sangat baik dalam mengatur item-item dalam satu baris (horizontal) ATAU satu kolom (vertikal).

Kegunaan: Sempurna untuk mengatur komponen-komponen kecil. Contohnya seperti:
- Membuat navbar di mana logo berada di kiri dan menu di kanan.
- Menyusun tombol-tombol agar memiliki jarak yang sama.
- Membuat konten di dalam sebuah kartu menjadi rata tengah secara vertikal.

2. Grid Layout

Konsep: Sistem layout dua dimensi. Grid memungkinkan kita untuk mengatur item dalam baris dan kolom secara bersamaan.

Kegunaan: Ideal untuk tata letak halaman secara keseluruhan. Contohnya seperti:
- Membuat galeri produk dengan 3 kolom dan beberapa baris.
- Mendesain layout halaman utama yang memiliki header, sidebar, konten utama, dan footer.
- Membuat struktur seperti majalah atau koran.

Kesimpulan: Gunakan Flexbox untuk mengatur elemen dalam satu baris/kolom (seperti menu atau tombol), dan gunakan Grid untuk mengatur layout halaman secara keseluruhan. Keduanya seringkali digunakan bersamaan dalam satu halaman.

E. - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! -
1. Implementasi Fungsi Backend: Saya memulai dengan mengerjakan logika di backend terlebih dahulu. Saya membuat fungsi edit_product dan delete_product di views.py, lalu mendaftarkan path-nya di urls.py. Saya pastikan kedua fungsi ini berjalan dengan benar sebelum lanjut ke frontend.

2. Struktur dan Kustomisasi Halaman Form: Selanjutnya, saya fokus pada halaman yang menggunakan form (tambah, edit, login, register). Saya membuka file HTML masing-masing, lalu menerapkan styling menggunakan kelas-kelas dari Tailwind CSS. Saya pastikan input field, label, dan tombol terlihat menarik dan konsisten.

3. Desain Ulang Halaman Detail: Saya membuka template halaman detail produk. Di sini, saya merombak total strukturnya agar lebih informatif, menambahkan bagian khusus untuk harga, stok, dan merek, serta memperbaiki tata letak deskripsi dan info author agar lebih rapi.

4. Desain Ulang Halaman Utama dan Kartu Produk: Ini adalah bagian terbesar.

Pertama, saya memodifikasi main.html untuk menambahkan logika {% if products %} dan {% else %} untuk menangani kondisi jika belum ada produk.

Kemudian, saya mendesain ulang file card_product.html secara total agar lebih cocok untuk e-commerce, dengan menonjolkan harga dan merek, serta memindahkan tombol Edit/Delete menjadi overlay yang muncul saat hover.

5. Pembuatan Navbar Responsif: Terakhir, saya membuat komponen navbar. Saya merancangnya dengan pendekatan desktop-first, lalu menambahkan kelas md:hidden dan hidden md:block untuk mengatur elemen mana yang muncul atau hilang di layar mobile. Saya juga menambahkan sedikit JavaScript untuk fungsionalitas tombol hamburger dan dropdown user.

6. Finishing dan Penulisan README: Setelah semua halaman terlihat bagus dan berfungsi di berbagai ukuran layar, saya melakukan pengujian akhir, lalu menjawab semua pertanyaan ini di file README.md.