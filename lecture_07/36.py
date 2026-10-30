with open("demo.txt", "r") as file1:
    content1 = file1.read()

with open("intro.txt", "r") as file2:
    content2 = file2.read()

with open("merged.txt", "w") as merged_file:
    merged_file.write(content1)
    merged_file.write("\n")
    merged_file.write(content2)

print("Files merged successfully!")
