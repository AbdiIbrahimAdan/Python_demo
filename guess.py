import random

print("Welcome to Number Guessing Game!")
secret_num = random.randint(1, 100)
guess = 0

while guess != secret_num:
    guess = int(input("Guess Number between 1 and 100: "))
    if guess < secret_num:
        print("Too Low!")
    elif guess > secret_num:
        print("Too High!")
    else:
        print("Congratulations! You guessed it right!")