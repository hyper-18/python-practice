name = (input("enter contact name:"))
num = int(input("enter phone number:"))
with open("contacts.txt", "a") as file:
    file.write(f"{name} - {num}\n")
print("saved")
