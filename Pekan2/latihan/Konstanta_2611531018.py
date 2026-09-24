# Buat file baru dengan nama Konstanta_NIM.py"
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI_1018: Final = 3.14
print("pi: %f" % (PI_1018))
jari_1018 = float(input('Masukkan nilai jari-jari: '))
luas_1018 = PI_1018 * jari_1018 * jari_1018
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1018, luas_1018))