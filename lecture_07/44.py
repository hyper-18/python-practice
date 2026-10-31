# Register a user
username = input("Create username: ")
password = input("Create password: ")

with open("users.txt", "w") as file:
    file.write(username + "," + password)

print("Registration successful!")

# Login
login_username = input("Enter username: ")
login_password = input("Enter password: ")

with open("users.txt", "r") as file:
    data = file.read()

stored_username, stored_password = data.split(",")

if login_username == stored_username and login_password == stored_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
