with open("student.txt", "r") as file:
    search_word = input("Enter the word to search: ")

    for line in file:
        if search_word.lower() in line.lower():
            print(line, end="")
