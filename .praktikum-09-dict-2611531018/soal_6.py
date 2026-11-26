jadwal = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a
hari_tersibuk = ""
jumlah_matkul_terbanyak = -1

for hari, daftar_matkul in jadwal.items():
    if len(daftar_matkul) > jumlah_matkul_terbanyak:
        jumlah_matkul_terbanyak = len(daftar_matkul)
        hari_tersibuk = hari

print(f"Busiest day: {hari_tersibuk} ({jumlah_matkul_terbanyak} courses)")

# 6b
nama_matkul = input().strip()
jumlah_hari = 0

for hari, daftar_matkul in jadwal.items():
    if nama_matkul in daftar_matkul:
        jumlah_hari += 1

print(f"{nama_matkul}: {jumlah_hari} days")