"Game that only completes when you guess the right number"

from random import randint

secret: int = randint(1,10)

guess: int = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    print("Wrong!")
    guess = int(input("Guess again: "))
    if guess > secret:
        print("Your guess was too high!")
    else: <= secret
        print("Your guess was too low!")
print("You got it!")