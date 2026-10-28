with open("student.txt", "r")as file:
    fitar_read = file.read(4)
    print("first read=", fitar_read)

    print("Pointer position=", file.tell())

    file.seek(0)

    second_read = file.read()
    print("second read=", second_read)
