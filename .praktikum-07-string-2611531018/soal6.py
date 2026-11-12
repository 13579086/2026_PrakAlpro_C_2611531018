# Name: <Habib Alhakim>
# NIM: <2611531018>
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


full_name = "Kartika"
nim = "2611531018"

clean = full_name.strip()

space = clean.find(" ")

first_name = clean[:space]

username = first_name.lower() + nim[-3:]

print(username)