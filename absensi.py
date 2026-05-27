import csv
import os
from datetime import datetime
import pytz

FILE_DATABASE = "database_absensi.csv"

def inisialisasi_database():
    if not os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Waktu", "NIM", "Nama", "Kelas", "Status Kehadiran"])

def absen_otomatis_server():
    nim = "SERVER-BOT"
    nama = "GitHub Actions"
    kelas = "Cloud-System"
    status = "Hadir"

    # Menggunakan zona waktu Asia/Jakarta agar jamnya akurat jam WIB
    timezone = pytz.timezone('Asia/Jakarta')
    waktu_sekarang = datetime.now(timezone)
    
    tanggal = waktu_sekarang.strftime("%Y-%m-%d")
    jam = waktu_sekarang.strftime("%H:%M:%S")

    try:
        with open(FILE_DATABASE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([tanggal, jam, nim, nama, kelas, status])
        print(f"✅ Sukses mencatat kehadiran otomatis pada {tanggal} - {jam}.")
    except Exception as e:
        print(f"❌ Gagal: {e}")

def main():
    inisialisasi_database()
    absen_otomatis_server()

if __name__ == "__main__":
    main()
