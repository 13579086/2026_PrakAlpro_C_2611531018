menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

# 1. Baca data dengan nested loop
for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        portion = int(input(f"Day {day}, {menu}: "))
        row.append(portion)
    sales.append(row)

# 2. Traversal per baris: total porsi setiap hari
print("Total per day:")
for r in range(len(sales)):
    day_total = 0
    for c in range(len(sales[r])):
        day_total += sales[r][c]
    print(f"Day {r + 1}: {day_total}")

# 3. Traversal per kolom: total porsi setiap menu dalam list of tuple
menu_totals = []
for c in range(len(menus)):
    menu_total = 0
    for r in range(len(sales)):
        menu_total += sales[r][c]
    menu_totals.append((menus[c], menu_total))

print("Total per menu:", menu_totals)

# 4. Cari menu terlaris (jika sama, pilih yang muncul lebih dulu)
best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")