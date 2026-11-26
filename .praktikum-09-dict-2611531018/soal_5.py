n = int(input())
kas = {}

for _ in range(n):
    bagian = input().split()
    nama = bagian[0]
    nominal = int(bagian[1])
    kas[nama] = kas.get(nama, 0) + nominal

for nama, total in kas.items():
    print(f"{nama}: {total}")
5
total_kas = sum(kas.values())
print(f"Total cash: {total_kas}")

penyetor_terbesar = ""
nominal_terbesar = -1

for nama, total in kas.items():
    if total > nominal_terbesar:
        nominal_terbesar = total
        penyetor_terbesar = nama

print(f"Top contributor: {penyetor_terbesar} ({nominal_terbesar})")