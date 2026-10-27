with open("intro.txt", "r") as file:
    content = file.read()
words = content.split()
count = len(words)
print("total words=", count)
