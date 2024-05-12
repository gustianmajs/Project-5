# Project 5

Project 5 adalah aplikasi Flask sederhana yang menggunakan Docker untuk mengelola multi-container environment. Aplikasi ini memiliki fitur dasar CRUD (Create, Read, Update, Delete) untuk entitas `User` yang disimpan dalam database PostgreSQL.

## Struktur Proyek

```
project-5/
│
├── app/
│   └── main.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt

```

- `docker-compose.yml`: File konfigurasi Docker Compose untuk menjalankan aplikasi dengan service database PostgreSQL dan service Flask.
- `Dockerfile`: File Dockerfile untuk membangun image Docker dari aplikasi Flask.
- `requirements.txt`: Daftar dependensi Python yang diperlukan oleh aplikasi.
- `app/main.py`: File utama aplikasi Flask yang berisi logika dan endpoint-endpoint HTTP.

## Instalasi dan Penggunaan

1. Pastikan Docker sudah terinstal di sistem Anda.
2. Clone repository ini ke dalam direktori lokal Anda.
3. Buka terminal dan arahkan ke direktori proyek.
4. Jalankan perintah berikut untuk membuat volume Docker yang diperlukan:

    ```bash
    docker volume create pg-data
    ```

5. Setelah itu, jalankan perintah berikut untuk membangun image Docker dari aplikasi:

    ```bash
    docker build -t project5 .
    ```

6. Terakhir, jalankan aplikasi dengan perintah:

    ```bash
    docker-compose up
    ```

Aplikasi akan dijalankan dan dapat diakses melalui `http://localhost:5000`.

## Endpoint Utama

- `/health`: Endpoint untuk mengecek status kesehatan aplikasi.
- `/db_check`: Endpoint untuk mengecek koneksi ke database.
- `/user`: Endpoint untuk operasi CRUD pada entitas `User`.
- `/user/<id>`: Endpoint untuk mendapatkan detail user berdasarkan ID.

## Kontribusi

Kontribusi dalam bentuk _pull request_ sangat dipersilakan. Silakan buka _issue_ untuk diskusi lebih lanjut.

## Lisensi

Diprogram dengan ❤️ oleh Gustian.
