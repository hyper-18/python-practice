with open("demo.txt", "r") as file1:
    content1 = file1.read()

with open("intro.txt", "r") as file2:
    content2 = file2.read()

if content1 == content2:
    print("Both files are identical.")
else:
    print("Both files are different.")
