while True:
    print("\n---NOTES APP---")
    print("ADD VIEW NOTES...")

    choice = input("enter what you want to do :")
    if choice == "add":
        note = input("enter your note:")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("NOTE SAVED")

    elif choice == "view":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

            if notes:
                print("\n---SAVED NOTES---")
                print(notes)
            else:
                print("NO NOTES FOUND.")
        except FileNotFoundError:
            print("NO NOTES FOUND.")
    elif choice == "exit":
        print("EXITING NOTES APP...")
        break
    else:
        print("INVALID ACTIONS")
