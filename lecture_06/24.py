marks = int(input("enter marks obtained:"))
total = int(input("enter total marks:"))


def percentage(marks, total):
    percent = (marks/total)*100
    print("percentage=", percent, "%")


percentage(marks, total)
