from datetime import datetime
current_time = datetime.now()
with open("contact.txt", "a") as file:
    file.write(str(current_time) + "\n")
print("saved")
