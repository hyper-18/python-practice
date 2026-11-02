while True:
    print("\n--- FILE HANDLING MENU ---")
    print("1. Write to File")
    print("2. Read File")
    print("3. Append to File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        content = input("Enter content to write: ")

        with open("student.txt", "w") as file:
            file.write(content + "\n")

        print("Content written successfully!")

    elif choice == "2":
        try:
            with open("student.txt", "r") as file:
                content = file.read()

            if content:
                print("\n--- FILE CONTENT ---")
                print(content)
            else:
                print("File is empty.")

        except FileNotFoundError:
            print("File does not exist.")

    elif choice == "3":
        content = input("Enter content to append: ")

        with open("student.txt", "a") as file:
            file.write(content + "\n")

        print("Content appended successfully!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
