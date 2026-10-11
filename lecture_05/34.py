text = input("Enter a string: ")

uppercase = 0
lowercase = 0

for character in text:
    if character.isupper():
        uppercase = uppercase + 1
    elif character.islower():
        lowercase = lowercase + 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
