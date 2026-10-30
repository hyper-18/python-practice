with open("student.txt", "r") as file:
    content = file.read()

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

updated_content = content.replace(old_word, new_word)

with open("student.txt", "w") as file:
    file.write(updated_content)

print("Word replaced successfully!")
