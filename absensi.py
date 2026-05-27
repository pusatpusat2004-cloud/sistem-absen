import csv
import os
from datetime import datetime

# Nama file database untuk menyimpan data absensi
FILE_DATABASE = "database_absensi.csv"

def inisialisasi_database():
    """Membuat file database CSV beserta headernya jika belum ada"""
    if not os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Waktu", "NIM", "Nama", "Kelas", "Status Kehadiran"])

def absen_otomatis_server():
    """Fungsi absensi otomatis tanpa meminta input mengetik"""
    # KARENA DIJALANKAN OLEH BOT, DATA KITA SET OTOMATIS DI SINI:
    nim = "SERVER-BOT"
    nama = "GitHub Actions"
    kelas = "Cloud-System"
    status = "Hadir"

    # Mengambil tanggal dan waktu saat ini
    waktu_sekarang = datetime.now()
    tanggal = waktu_sekarang.strftime("%Y-%m-%d")
    jam = waktu_sekarang.strftime("%H:%M:%S")

    try:
        with open(FILE_DATABASE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([tanggal, jam, nim, nama, kelas, status])
        print(f"✅ Sukses! Bot berhasil mencatat kehadiran otomatis pada {tanggal} jam {jam}.")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}")

def main():
    inisialisasi_database()
    # Langsung jalankan fungsi otomatis tanpa menu pilihan
    absen_otomatis_server()

if __name__ == "__main__":
    main()
