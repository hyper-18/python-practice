with open("student.txt", "r")as file:
    content = file.read(4)
    print("first read:", content)

    file.seek(0)
    content = file.read(4)
    print("second read:", content)
