number_of_rows = 4
seats_per_row = 5
# Write your code below

seats = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
    for r in range(number_of_rows):
        row_str = ""
        for c in range(seats_per_row):
            if c > 0:
                row_str += " "
            row_str += seats[r][c]
        print(f"Row {r + 1}: {row_str}")

    row_input = int(input("Row (0 to stop): "))
    if row_input == 0:
        break

    seat_input = int(input("Seat: "))

    if row_input < 1 or row_input > number_of_rows or seat_input < 1 or seat_input > seats_per_row:
        print("Invalid seat.")
    elif seats[row_input - 1][seat_input - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_input - 1][seat_input - 1] = "X"
        print("Seat booked.")

taken_count = 0
for r in range(number_of_rows):
    for c in range(seats_per_row):
        if seats[r][c] == "X":
            taken_count += 1

print(f"Seats taken: {taken_count}")