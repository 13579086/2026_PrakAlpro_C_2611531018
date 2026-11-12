# Name: <Habib Alhakim>
# NIM: <2611531018>
# Question 5

username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

NIM = input("NIM: ")

if len(NIM) == 10 and NIM.isdigit():
    intake_year = NIM[:2]
    print("Valid, intake year 20" + intake_year)
else:
    print("Invalid NIM")