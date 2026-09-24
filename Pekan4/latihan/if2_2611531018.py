# Buat file dengan nama if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()  

ipk_1018 = float(input("Masukkan IPK Anda: ")) 
 
if ipk_1018 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_1018))
else:
    print("Anda tidak lulus")
print("Program Selesai")