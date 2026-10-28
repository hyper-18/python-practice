with open("student.txt", "r")as file:
    print("position:", file.tell())
    content = file.read(4)
    print("content:", content)
    print("position:", file.tell())
