# Program Kasir & Hitung Diskon Sederhana

total_belanja = float(input("Masukkan total belanja (Rp): "))

# Cek apakah dapat diskon (diskon 10% jika belanja di atas 100.000)
if total_belanja > 100000:
    diskon = total_belanja * 0.10
    total_bayar = total_belanja - diskon
    print("Selamat! Kamu mendapatkan diskon 10%.")
else:
    diskon = 0
    total_bayar = total_belanja
    print("Maaf, kamu belum dapat diskon.")

print(f"Potongan harga : Rp {diskon:,.0f}")
print(f"Total bayar     : Rp {total_bayar:,.0f}")