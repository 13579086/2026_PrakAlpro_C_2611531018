# Name: <Habib Alhakim>
# NIM: <2611531018>
# Question 4

phone = "082611531018"

first_part = phone[:4]
last_part = phone[-3:]
hidden_count = len(phone) - len(first_part) - len(last_part)

masked = first_part + "*" * hidden_count + last_part
print(masked)

phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)
