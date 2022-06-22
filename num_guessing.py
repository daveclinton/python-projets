import random

# a function guessing_game with no arguments

def guessing_game():
    number = random.randint(10,30)

    while True:
        user_value = int(input("What is your age? "))

        if user_value == number:
            print(f"Your guess of {user_value} is right")
            break
        if user_value < number:
            print(f"Your guess of {user_value} is too low")

        else:
            print(f"Your guess of {user_value} is too high")


guessing_game()