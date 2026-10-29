with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("longest word:", longest_word)
print("length:", len(longest_word))
