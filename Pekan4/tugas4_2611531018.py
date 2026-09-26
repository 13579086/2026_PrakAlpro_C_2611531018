import sys

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_1018 = input("Masukkan Nama Pengunjung        : ")
umur_1018 = int(input("Input umur anda                 : "))
sim_1018 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
if sim_1018:
    sim_1018 = sim_1018[0]

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_1018 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_1018 = int(input("Masukkan jumlah tiket           : "))

# Validation: if tunggal
if jumlah_tiket_1018 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    sys.exit()

is_member_1018 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_1018 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# 2. Pemilihan Wahana Menggunakan match-case
nama_wahana_1018 = ""
harga_satuan_1018 = 0

match paket_1018:
    case 1:
        nama_wahana_1018 = "Wahana Safari Rimba"
        harga_satuan_1018 = 50000
    case 2:
        nama_wahana_1018 = "Wahana Arung Jeram"
        harga_satuan_1018 = 75000
    case 3:
        nama_wahana_1018 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1018 = 120000
    case 4:
        nama_wahana_1018 = "Wahana Roller Coaster Kilat"
        harga_satuan_1018 = 100000
    case 5:
        nama_wahana_1018 = "Wahana All-Access VIP"
        harga_satuan_1018 = 220000
    case _:
        print("Paket wahana tidak valid!")
        sys.exit()

# 3. Validasi Izin Kendali Wahana Menggunakan if-elif-else dan Operator Logika
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_1018 == 3:
    if umur_1018 >= 17 and sim_1018 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_1018 >= 17 and sim_1018 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_1018 < 17 and sim_1018 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_1018 >= 10:
        print("Status Akses: Pengunjung memenuhi syarat umur untuk wahana ini.")
    else:
        print("Status Akses: Pengunjung belum memenuhi syarat umur minimum wahana (min. 10 tahun).")

# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
subtotal_1018 = harga_satuan_1018 * jumlah_tiket_1018
total_diskon_persen_1018 = 0

if subtotal_1018 >= 200000:
    total_diskon_persen_1018 += 10

if is_member_1018 in ['y', 'ya']:
    total_diskon_persen_1018 += 5

if kode_promo_valid_1018 in ['y', 'ya']:
    total_diskon_persen_1018 += 15

if jumlah_tiket_1018 >= 5:
    total_diskon_persen_1018 += 5

# 5. Evaluasi Kelulusan Audit Menggunakan if-else
nominal_diskon_1018 = subtotal_1018 * (total_diskon_persen_1018 / 100)
total_bayar_1018 = subtotal_1018 - nominal_diskon_1018

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_1018:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_1018}% (Rp {nominal_diskon_1018:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_1018:,.0f}")

if total_bayar_1018 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("Program Selesai")