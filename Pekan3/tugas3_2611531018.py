# ==============================================================================
# TUGAS PEKAN 3 - SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
# Variabel diakhiri dengan 4 digit terakhir NIM: 1018
# ==============================================================================

print("=== SISTEM TRANSAKSI TOKO ===")

# --- 1. INPUT DATA PELANGGAN DAN TRANSAKSI ---
nama_1018 = input("Masukkan Nama Pelanggan : ")
status_1018 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1018 = float(input("Masukkan Total Belanja : "))
jumlah_barang_1018 = int(input("Masukkan Jumlah Barang : "))
kode_promo_1018 = input("Masukkan Kode Promo : ")

# --- 2. OPERATOR KEANGGOTAAN (MEMBERSHIP) ---
daftar_promo_1018 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
# Penggunaan operator 'in' dan 'not in'
promo_tersedia_1018 = kode_promo_1018 in daftar_promo_1018
promo_tidak_valid_1018 = kode_promo_1018 not in daftar_promo_1018

# --- 3. OPERATOR PERBANDINGAN & LOGIKA ---
# Operator Perbandingan (>=, ==)
syarat_belanja_1018 = total_belanja_1018 >= 200000
syarat_barang_1018 = jumlah_barang_1018 >= 3
is_member_1018 = status_1018 == "member"

# Operator Logika (and, or, not)
dapat_diskon_1018 = is_member_1018 and syarat_belanja_1018
dapat_promo_1018 = (promo_tersedia_1018 and syarat_barang_1018) or (is_member_1018 and promo_tersedia_1018)
bukan_member_1018 = not is_member_1018

# --- 4. OPERATOR ARITMATIKA & PENUGASAN ---
# Menentukan besarnya diskon (10% jika dapat diskon)
besaran_diskon_1018 = total_belanja_1018 * 0.10 if dapat_diskon_1018 else 0.0

# Total pembayaran awal
total_pembayaran_1018 = total_belanja_1018 - besaran_diskon_1018

# Rata-rata harga barang (pembagian /)
rata_rata_harga_1018 = total_belanja_1018 / jumlah_barang_1018

# Sisa pembagian (modulus %) untuk simulasi nomor antrean/kupon
sisa_poin_1018 = int(total_belanja_1018) % 1000

# Operator Penugasan / Augmented Assignment (-= dan +=)
# Mengurangi total pembayaran jika promo valid
if promo_tersedia_1018:
    total_pembayaran_1018 -= 5000  # Potongan tambahan promo Rp5.000

# Menambah poin pelanggan
poin_1018 = 0
poin_1018 += int(total_pembayaran_1018 // 10000)

# --- 5. OPERATOR IDENTITAS (IDENTITY) ---
# Membandingkan identitas objek (is / is not)
status_obj1_1018 = is_member_1018
status_obj2_1018 = is_member_1018
identitas_sama_1018 = status_obj1_1018 is status_obj2_1018
identitas_beda_1018 = status_obj1_1018 is not total_belanja_1018

# --- 6. OPERATOR BITWISE ---
# Penentuan Bit Status:
# Bit 0 (0001 = 1) : Member
# Bit 1 (0010 = 2) : Total belanja >= Rp200.000
# Bit 2 (0100 = 4) : Jumlah barang >= 3
# Bit 3 (1000 = 8) : Kode promo tersedia

bit_member_1018 = 1 if is_member_1018 else 0
bit_belanja_1018 = 2 if syarat_belanja_1018 else 0
bit_barang_1018 = 4 if syarat_barang_1018 else 0
bit_promo_1018 = 8 if promo_tersedia_1018 else 0

# Operator Bitwise OR (|) untuk menggabungkan status
kode_status_1018 = bit_member_1018 | bit_belanja_1018 | bit_barang_1018 | bit_promo_1018

# Operator Bitwise AND (&) untuk mengecek kondisi
cek_member_1018 = kode_status_1018 & 1
cek_promo_1018 = kode_status_1018 & 8

# Operator Bitwise XOR (^) untuk membandingkan dengan kode referensi (1011 desimal = 11)
kode_referensi_1018 = 11
hasil_xor_1018 = kode_status_1018 ^ kode_referensi_1018

# Operator Bitwise Shift (<<)
hasil_shift_1018 = kode_status_1018 << 1


# ==============================================================================
# DISPLAY OUTPUT HASIL PROGRAM
# ==============================================================================

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_1018}")
print(f"Status Pelanggan      : {status_1018}")
print(f"Total Belanja         : Rp{int(total_belanja_1018)}")
print(f"Jumlah Barang         : {jumlah_barang_1018}")
print(f"Kode Promo            : {kode_promo_1018}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000         : {syarat_belanja_1018}")
print(f"Jumlah Barang >= 3          : {syarat_barang_1018}")
print(f"Status Member               : {is_member_1018}")
print(f"Kode Promo Tersedia         : {promo_tersedia_1018}")
print(f"Mendapatkan Diskon          : {dapat_diskon_1018}")
print(f"Mendapatkan Promo           : {dapat_promo_1018}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                      : Rp{int(besaran_diskon_1018)}")
print(f"Total Pembayaran            : Rp{int(total_pembayaran_1018)}")
print(f"Rata-rata Harga Barang      : Rp{rata_rata_harga_1018:.2f}")
print(f"Sisa Modulus Belanja        : {sisa_poin_1018}")
print(f"Poin Terkumpul (+=)         : {poin_1018}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : {bin(kode_status_1018)[2:].zfill(4)}")
print(f"Member Access               : {cek_member_1018 > 0}")
print(f"Promo Access                : {cek_promo_1018 > 0}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {bin(kode_status_1018)[2:].zfill(4)}")
print(f"Kode Desimal  : {kode_status_1018}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kode_status_1018)[2:].zfill(4)} & 0001")
print(f"Hasil Biner   : {bin(cek_member_1018)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_member_1018}")

print("\nCek Promo")
print(f"{bin(kode_status_1018)[2:].zfill(4)} & 1000")
print(f"Hasil Biner   : {bin(cek_promo_1018)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_promo_1018}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(kode_status_1018)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_1018)[2:].zfill(4)}")
print(f"{bin(kode_status_1018)[2:].zfill(4)} ^ {bin(kode_referensi_1018)[2:].zfill(4)}")
print(f"Hasil Biner   : {bin(hasil_xor_1018)[2:].zfill(4)}")
print(f"Hasil Desimal : {hasil_xor_1018}")

print("\n=== Shift ===")
print(f"{bin(kode_status_1018)[2:].zfill(4)} << 1")
print(f"Hasil Biner   : {bin(hasil_shift_1018)[2:]}")
print(f"Hasil Desimal : {hasil_shift_1018}")

print("\n=== SELESAI ===")