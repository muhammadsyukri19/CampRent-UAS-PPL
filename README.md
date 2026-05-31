# CampRent - Aplikasi Penyewaan Alat Camping

Proyek ini adalah sistem informasi penyewaan alat camping (CampRent) yang dibangun menggunakan framework **Django (Python)**. Aplikasi ini merupakan tugas akhir (Final Stage) untuk mata kuliah **Proyek Perangkat Lunak**.

## 🚀 Fitur Utama

Aplikasi ini dibagi menjadi dua bagian utama:

### 1. Halaman Pengguna (Public)
Halaman ini dapat diakses oleh siapa saja tanpa perlu login.
- **Landing Page**: Halaman utama aplikasi.
- **Katalog Alat**: Menampilkan daftar alat camping yang tersedia untuk disewa.
- **Detail Alat**: Informasi lengkap mengenai alat tertentu.
- **Formulir Booking**: Fitur bagi pengguna untuk menyewa alat camping.

### 2. Dashboard Admin
Halaman ini dikhususkan untuk admin pengelola dan **wajib login**.
- **Autentikasi**: Login dan Logout admin.
- **Manajemen Alat (CRUD)**: Admin dapat melihat daftar alat, menambahkan alat baru, mengedit informasi alat, dan menghapus alat.
- **Manajemen Booking**: Admin dapat melihat daftar pesanan, mengubah status pesanan (Pending, Dipinjam, Selesai), dan menghapus riwayat pesanan.

## 🛠️ Teknologi yang Digunakan

- **Backend Framework**: Django (Python)
- **Database**: SQLite (Default bawaan Django)
- **Frontend**: HTML, CSS, JavaScript (terintegrasi dalam Django Templates)
- **Arsitektur**: MVT (Model-View-Template) standar Django

## 📂 Struktur Folder Utama

```text
CampRent-UAS-PPL/
├── camprent/           # Konfigurasi utama project Django (settings, urls, asgi, wsgi)
├── media/              # Folder untuk menyimpan file upload (gambar alat camping)
├── rental/             # Aplikasi utama (App Django)
│   ├── migrations/     # File migrasi database
│   ├── static/         # File statis (CSS, JS, Images)
│   ├── templates/      # File HTML (Public & Admin Dashboard)
│   ├── admin.py        # Konfigurasi admin bawaan Django
│   ├── forms.py        # Form input data
│   ├── models.py       # Struktur database (Equipment, Booking)
│   ├── urls.py         # Routing URL khusus app rental
│   └── views.py        # Logika sistem aplikasi
├── db.sqlite3          # File database SQLite
├── manage.py           # Script manajemen command-line Django
└── README.md           # Dokumentasi proyek ini
```

## 💻 Panduan Instalasi dan Penggunaan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini secara lokal:

### Persyaratan
- Python 3.8 atau yang lebih baru
- `pip` (Python package installer)

### Langkah Instalasi
1. **Clone Repository**
   ```bash
   git clone <link-repository-github>
   cd CampRent-UAS-PPL
   ```

2. **Buat Virtual Environment (Opsional tapi disarankan)**
   ```bash
   python -m venv venv
   # Aktivasi (Windows)
   venv\Scripts\activate
   # Aktivasi (Mac/Linux)
   source venv/bin/activate
   ```

3. **Install Dependencies**
   Pastikan Anda menginstal Django dan library pendukung (seperti Pillow untuk image field).
   ```bash
   pip install django pillow
   ```

4. **Jalankan Migrasi Database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Buat Akun Superuser (Admin)**
   Agar bisa mengakses Dashboard Admin, Anda perlu membuat akun admin.
   ```bash
   python manage.py createsuperuser
   ```
   *Ikuti instruksi untuk mengisi username, email, dan password.*

6. **Jalankan Server Lokal**
   ```bash
   python manage.py runserver
   ```

7. **Akses Aplikasi**
   - **Halaman Public**: Buka `http://127.0.0.1:8000/` di browser.
   - **Dashboard Admin**: Buka `http://127.0.0.1:8000/admin-login/` untuk login ke dashboard custom. *(Catatan: Anda juga dapat mengakses admin default Django di `/admin/`)*.

## 🎥 Video Presentasi
Link video presentasi yang menjelaskan fitur, arsitektur, struktur folder, dan demo aplikasi:
- **[Masukkan Link YouTube/Drive Anda Di Sini]**

## ✅ Penilaian & Persyaratan (Checklist)

Aplikasi ini telah memenuhi seluruh kriteria tugas Final Stage:
- [x] Menggunakan salah satu framework yang diizinkan (**Django**).
- [x] Memiliki Halaman Umum (Landing page, Katalog, Booking) tanpa perlu login.
- [x] Memiliki Dashboard Admin yang terlindungi oleh sistem login.
- [x] Mendukung fungsi CRUD (Create, Read, Update, Delete) pada entitas Alat dan Manajemen Booking.
- [x] Menyertakan file `README.md` dengan panduan instalasi lengkap.

---
**Dibuat untuk Tugas Final Stage Mata Kuliah Proyek Perangkat Lunak.**
