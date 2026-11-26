absen_kelas = input().split()
absen_yang_ngumpul = input().split()

absen_yang_ngumpul_set = set(absen_yang_ngumpul)
absen_kelas_set = set(absen_kelas)

belum_kumpul = absen_kelas_set - absen_yang_ngumpul_set

print(f"Submitted: {len(absen_yang_ngumpul_set)} students")
print(f"Not submitted: {len(belum_kumpul)} students")

for absen in absen_kelas:
    if absen not in absen_yang_ngumpul_set:
        print(absen)