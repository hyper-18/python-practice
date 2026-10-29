with open("student.txt", "r") as file:
    content = file.read()
search_word = input("enter a word to count")
words = content.split()
count = 0
for word in words:
    if word.lower() == search_word.lower():
        count += 1
print("occurrence:", count)
