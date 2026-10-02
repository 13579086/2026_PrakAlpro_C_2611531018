# Program Kasir & Hitung Diskon Sederhana

total_belanja_1018 = float(input("Masukkan total belanja (Rp): "))

# Cek apakah dapat diskon (diskon 10% jika belanja di atas 100.000)
if total_belanja_1018 > 100000:
    diskon_1018 = total_belanja_1018 * 0.10
    total_bayar_1018 = total_belanja_1018 - diskon_1018
    print("Selamat! Kamu mendapatkan diskon 10%.")
else:
    diskon_1018 = 0
    total_bayar_1018 = total_belanja_1018
    print("Maaf, kamu belum dapat diskon.")

print(f"Potongan harga : Rp {diskon_1018:,.0f}")
print(f"Total bayar     : Rp {total_bayar_1018:,.0f}")