# Buat file dengan nama nested_for1_1018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1018
# Program ini menggunakan fungsi input()

batas_1018 = int(input("Masukkan nilai batas: "))

for line_1018 in range(1, batas_1018 + 1):
    for j_1018 in range(1, (-1 * line_1018 + batas_1018) + 1):
        print(".", end="")
    print(line_1018)