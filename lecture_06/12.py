year = int(input("enter a year:"))


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(2024))
print(is_leap_year(2025))
print(is_leap_year(2000))
print(is_leap_year(1900))
