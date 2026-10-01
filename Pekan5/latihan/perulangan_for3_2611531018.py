# Buat file dengan nama perulangan_for3_1018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1018
# Program ini menggunakan fungsi input()

ulang_1018 = int(input("Masukkan jumlah perulangan: "))

jumlah_1018 = 0
for i_1018 in range(1, ulang_1018 + 1):
    print(i_1018, end=" ")
    jumlah_1018 = jumlah_1018 + i_1018

    if i_1018 < ulang_1018:
        print("+ ", end="")
    else:
        print(" = ", jumlah_1018, end="")
        
print()
print("Jumlah = ", jumlah_1018)