text = input('enter a word:').lower()
count = 0
for character in text:
    if character in "aeiou":
        count = count+1
print(count)
