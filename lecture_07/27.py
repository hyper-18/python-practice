with open("student.txt", "r") as file:
    content = file.read()
search_word = input("enter a word to search:")
if search_word.lower() in content.lower():
    print("word found")
else:
    print("word not found")
