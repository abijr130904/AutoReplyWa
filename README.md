## WA Auto-Reply dengan AI Lokal

Proyek ini memungkinkan kamu membuat bot WhatsApp yang dapat membalas pesan secara otomatis menggunakan AI lokal berbasis model GPT-2 atau GPT-2 fine-tuned untuk bahasa Indonesia.

## Fitur

Balas pesan WhatsApp secara otomatis.
Balasan cepat tidak panjang dan kadang gak nyambung 
Menggunakan model AI lokal tanpa perlu koneksi internet (setelah model diunduh).
Bisa menggunakan model chatbot khusus bahasa Indonesia
Dapat dijalankan di CPU.

## Persyaratan
Python ≥ 3.10
Sistem operasi: Windows / Linux / Mac
WhatsApp Web (untuk scanning QR code)
Internet untuk mengunduh model pertama kali.

## Instalasi
Clone repository proyek
Siapkan virtual environment (opsional tapi disarankan)
## bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

## Install semua dependensi
## bash
Lalu jalankan:

pip install -r requirements.txt
Download model AI lokal
Contoh: cahya/gpt2-small-indonesian-522M atau IzzulGod/GPT2-Indo-Instruct-Tuned
Pastikan tersimpan di folder cache atau bisa diakses dari transformers.

## Jalankan file utama:
## bash
python main.py

Scan QR code WhatsApp Web di browser.
Mulai chat di WhatsApp, bot akan membalas pesan secara otomatis.

## Struktur Proyek
wa-auto-reply/
│
├─ main.py           # File utama menjalankan bot WA
├─ ai_module.py      # Modul untuk memanggil AI Lokal
├─ requirements.txt  # Daftar package yang dibutuhkan
├─ README.md         # Dokumentasi ini
