# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1018 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1018 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_1018)
print("A2 =", a2_1018)

# Konjungsi: bernilai True jika keduanya True
hasil_1018 = a1_1018 and a2_1018
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1018)

# Disjungsi: bernilai True jika salah satunya True
hasil_1018 = a1_1018 or a2_1018
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_1018)

# Negasi A1: membalik nilai A1
hasil_1018 = not a1_1018
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1018)

# Negasi A2: membalik nilai A2
hasil_1018 = not a2_1018
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1018)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1018 = a1_1018 != a2_1018
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1018)