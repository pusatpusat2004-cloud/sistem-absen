import csv
import os
from datetime import datetime
import pytz

FILE_DATABASE = "database_absensi.csv"

def inisialisasi_database():
    """Membuat file database CSV beserta headernya jika belum ada"""
    if not os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Waktu", "NIM", "Nama", "Kelas", "Status Kehadiran"])

def input_absensi_manual():
    """Fungsi agar kamu bisa mengetik data absensi sendiri"""
    print("\n=====================================")
    print("        FORM INPUT ABSENSI MANUAl    ")
    print("=====================================")
    
    # Kamu ketik sendiri di sini nanti:
    nim = input("Masukkan NIM   : ").strip()
    nama = input("Masukkan Nama  : ").strip()
    kelas = input("Masukkan Kelas : ").strip()
    
    print("\nStatus Kehadiran:")
    print("1. Hadir")
    print("2. Izin")
    print("3. Sakit")
    pilihan_status = input("Pilih status (1/2/3): ").strip()
    
    if pilihan_status == "1":
        status = "Hadir"
    elif pilihan_status == "2":
        status = "Izin"
    elif pilihan_status == "3":
        status = "Sakit"
    else:
        print("❌ Pilihan status tidak valid! Absensi dibatalkan.")
        return

    # Waktu otomatis Jakarta (WIB)
    timezone = pytz.timezone('Asia/Jakarta')
    waktu_sekarang = datetime.now(timezone)
    tanggal = waktu_sekarang.strftime("%Y-%m-%d")
    jam = waktu_sekarang.strftime("%H:%M:%S")

    try:
        with open(FILE_DATABASE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([tanggal, jam, nim, nama, kelas, status])
        print(f"\n✅ Sukses! Absensi {nama} ({nim}) berhasil disimpan secara manual.")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}")

def main():
    inisialisasi_database()
    input_absensi_manual()

if __name__ == "__main__":
    main()
