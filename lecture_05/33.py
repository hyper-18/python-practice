text = input("Enter a string: ").lower()

count = 0

for character in text:
    if character == "a":
        count = count + 1

print("Occurrences of a:", count)
