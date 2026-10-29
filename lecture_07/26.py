with open("student.txt", "r") as file:
    content = file.read()
words = content.split()
shrt_word = words[0]
for word in words:
    if len(word) < len(shrt_word):
        shrt_word = word
print("shortest word:", shrt_word)
print("length:", len(shrt_word))
