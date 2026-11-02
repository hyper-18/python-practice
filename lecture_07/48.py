with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

with open("unique_words.txt", "w") as file:
    for word in unique_words:
        file.write(word + "\n")

print("Unique words saved successfully!")
