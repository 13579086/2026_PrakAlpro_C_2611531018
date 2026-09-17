from typing import Final

BATAS_LULUS_1018: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_1018 = input("Masukkan Nama Mahasiswa : ")
jk_1018 = input("Masukkan Jenis Kelamin (L/P): ")

umur_1018 = int(input("Masukkan Umur : "))
skor_1018 = float(input("Masukkan Skor Tes Awal : "))

alamat_1018 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

token_1018 = 100 + 3j

status_1018 = skor_1018 >= BATAS_LULUS_1018

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print(f"Nama Mahasiswa : {nama_1018} | Tipe: {type(nama_1018)}")
print(f"Jenis Kelamin  : {jk_1018} | Tipe: {type(jk_1018)}")
print(f"Alamat Domisili:\n{alamat_1018} | Tipe: {type(alamat_1018)}")
print(f"Umur           : {umur_1018} tahun | Tipe: {type(umur_1018)}")
print(f"Skor Tes Awal  : {skor_1018} | Tipe: {type(skor_1018)}")
print(f"ID Token Sinyal: {token_1018} | Tipe: {type(token_1018)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS_1018}")
print(f"Apakah Dinyatakan Lulus?: {status_1018} | Tipe: {type(status_1018)}")