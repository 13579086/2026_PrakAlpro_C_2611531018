#Buat file baru dengan nama Boolean_NIM.py
#nama variabel ditambah 4 digit nim terakhir contoh: nilai_5500
# Deklarasikan variabel dengan tipe data Boolean
is_lulus_1018 = True
is_cumlaude_1018 = True

# Menggunakan Boolean
nilai_1018 = 85
batas_lulus_1018 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_1018 = nilai_1018 >= batas_lulus_1018 #Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_1018)
print("Apakah lulus?:", status_kelulusan_1018)
if is_lulus_1018 and is_cumlaude_1018:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")