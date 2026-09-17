# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_1018 = int(input("Input angka-1: "))
angka2_1018 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_1018)
print("Nilai angka2 =", angka2_1018)

# Assignment biasa
hasil_1018 = angka1_1018
print("\nAssignment biasa (=)")
print("Hasil =", hasil_1018)

# Assignment penambahan
hasil_1018 = angka1_1018
hasil_1018 += angka2_1018
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_1018)

# Assignment pengurangan
hasil_1018 = angka1_1018
hasil_1018 -= angka2_1018
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_1018)

# Assignment perkalian
hasil_1018 = angka1_1018
hasil_1018 *= angka2_1018
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_1018)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1018 != 0:
    hasil_1018 = angka1_1018
    hasil_1018 /= angka2_1018
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_1018)
    # Operator tambahan
    hasil_1018 = angka1_1018
    hasil_1018 //= angka2_1018
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_1018)
    hasil_1018 = angka1_1018
    hasil_1018 %= angka2_1018
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_1018)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_1018 = angka1_1018
hasil_1018 **= angka2_1018
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_1018)