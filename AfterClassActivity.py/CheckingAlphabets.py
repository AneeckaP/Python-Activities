char = input("Enter a character: ")
if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(char, "is an alphabet.")
else:
    print(char, "is not an alphabet.")