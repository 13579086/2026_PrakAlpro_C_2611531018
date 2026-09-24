# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1018 = int(input("Input angka-1: "))
angka2_1018 = int(input("Input angka-2: "))

# Penjumlahan
hasil_1018 = angka1_1018 + angka2_1018
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1018)

# Pengurangan
hasil_1018 = angka1_1018 - angka2_1018
print("\nOperator Pengurangan")
print("Hasil =", hasil_1018)

# Perkalian
hasil_1018 = angka1_1018 * angka2_1018
print("\nOperator Perkalian")
print("Hasil =", hasil_1018)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1018 != 0:
    hasil_1018 = angka1_1018 / angka2_1018
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1018)

    hasil_1018 = angka1_1018 // angka2_1018
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1018)

    hasil_1018 = angka1_1018 % angka2_1018
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1018)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_1018 = angka1_1018 ** angka2_1018
print("\nOperator Pangkat")
print("Hasil =", hasil_1018)