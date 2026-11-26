absen_kelas = input().split()
absen_yang_ngumpul = input().split()

sudah_kumpul = set(absen_yang_ngumpul)
kelas_set = set(absen_kelas)

belum_kumpul = kelas_set - sudah_kumpul

print(f"Submitted: {len(sudah_kumpul)} students")
print(f"Not submitted: {len(belum_kumpul)} students")

for absen in absen_kelas:
    if absen not in sudah_kumpul:
        print(absen)