name_input = "Habib Alhakim"
NIM = "2611531018"

name = name_input.title()
space = name.find(" ")

if space == -1:
    first_name = name
else:
    first_name = name[:space]

username = first_name.lower() + NIM[-3:]
intake = "20" + NIM[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name}")
print(f"{'NIM':<10}: {NIM}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)