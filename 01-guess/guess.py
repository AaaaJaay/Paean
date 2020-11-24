import random


def get_guess():
    guess = None
    while guess is None:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Enter an integer please")
    return guess

number = random.randint(0, 99)
print("I've thought of a number between 0 and 99. Try to guess it")

guess = get_guess()
while guess != number:
    if guess > number:
        print("Nope! Guess a lower number")
    elif guess < number:
        print("Nope! Guess a higher number")
    guess = get_guess()

print(f"You got it, it was {number}")
