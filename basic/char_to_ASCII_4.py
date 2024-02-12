# Python 3 program to print ASCII value of string
print("Enter a String: ", end="")
text = input()
textlenght = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)

