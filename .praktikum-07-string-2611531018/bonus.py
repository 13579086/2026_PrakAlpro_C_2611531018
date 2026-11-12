sentence = input("Masukkan kalimat: ")

clean = sentence.lower().replace(" ", "")

reversed = clean[::-1]

if clean == reversed and len(clean) > 0:
    print("Palindrome")
else:
    print("Not a palindrome")