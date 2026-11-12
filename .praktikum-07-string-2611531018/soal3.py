# Name: <Habib Alhakim>
# NIM: <2611531018>
# Question 3

text = "Informatika"
print(text[-1])
print(text.upper())
print(text[0:20])

text = "Habib Alhakim"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
