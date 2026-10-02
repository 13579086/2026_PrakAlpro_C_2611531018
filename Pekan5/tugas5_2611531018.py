n_1018 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("#", end="")
for i_1018 in range(4 * n_1018 + 5):
    print("=", end="")
print("#")

for baris_1018 in range(n_1018, 0, -1):
    print("| ", end="")
    
    for spasi_1018 in range(2 * (n_1018 - baris_1018)):
        print(" ", end="")
        
    for angka_1018 in range(baris_1018, 0, -1):
        print(angka_1018, end=" ")
        
    print("<*>", end="")
    
    for angka_1018 in range(1, baris_1018 + 1):
        print("", angka_1018, end="")
        
    for spasi_1018 in range(2 * (n_1018 - baris_1018)):
        print(" ", end="")
        
    print(" |")

print("|", end="")
for spasi_1018 in range(2 * n_1018 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_1018 in range(2 * n_1018 + 1):
    print(" ", end="")
print("|")

for baris_1018 in range(1, n_1018    + 1):
    print("| ", end="")
    
    for spasi_1018 in range(2 * (n_1018 - baris_1018)):
        print(" ", end="")
        
    for angka_1018 in range(baris_1018, 0, -1):
        print(angka_1018, end=" ")
        
    print("<*>", end="")
    
    for angka_1018 in range(1, baris_1018 + 1):
        print("", angka_1018, end="")
        
    for spasi_1018 in range(2 * (n_1018 - baris_1018)):
        print(" ", end="")
        
    print(" |")

print("#", end="")
for i_1018 in range(4 * n_1018 + 5):
    print("=", end="")
print("#")