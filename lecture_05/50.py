secret_num = 67
guess = int(input("guess the number: "))
while guess != secret_num:
    if guess < secret_num:
        print("too low")
    else:
        print("too high")
    guess = int(input("guess again: "))
print("correct", secret_num)
