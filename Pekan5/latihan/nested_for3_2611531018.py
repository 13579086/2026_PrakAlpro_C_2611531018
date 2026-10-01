# Buat file dengan nama nested_for4_1018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1018
# Program ini menggunakan fungsi input()

tinggi_1018 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1018 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1018 = tinggi_1018
    c_1018 = a_1018
    lebar_1018 = (2 * tinggi_1018) - 2

    for i_1018 in range(1, tinggi_1018 + 1):
        b_1018 = c_1018 + 1

        for j_1018 in range(1, lebar_1018 + 1):

            # Baris atas dan bawah
            if i_1018 == 1 or i_1018 == tinggi_1018:
                if j_1018 == 1 or j_1018 == lebar_1018:
                    print("*", end="")
                else:
                    print("-", end="")

            # Baris isi
            else:
                if j_1018 == 1 or j_1018 == lebar_1018:
                    print("|", end="")
                else:
                    if j_1018 == c_1018:
                        print("<", end="")
                    elif j_1018 == b_1018:
                        print(">", end="")
                    elif j_1018 == (lebar_1018 - c_1018):
                        print("<", end="")
                    elif j_1018 == (lebar_1018 - c_1018 + 1):
                        print(">", end="")
                    elif j_1018 > b_1018 and j_1018 < (lebar_1018 - c_1018):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_1018 -= 2

        if a_1018 <= 0:
            c_1018 = (-a_1018) + 2
        else:
            c_1018 = a_1018