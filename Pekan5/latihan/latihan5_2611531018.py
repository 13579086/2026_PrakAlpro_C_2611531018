# Program untuk menampilkan pola segitiga piramida
# Nama variabel ditambah 4 digit NIM terakhir: 1018

tinggi_1018 = int(input("Masukkan tinggi segitiga: "))

for i_1018 in range(1, tinggi_1018 + 1):
    # Cetak spasi di sebelah kiri agar pola sejajar di tengah
    for j_1018 in range(tinggi_1018 - i_1018):
        print(" ", end="")
    
    # Cetak bintang beserta spasi
    for k_1018 in range(i_1018):
        print("*", end=" ")
    
    # Pindah baris
    print()