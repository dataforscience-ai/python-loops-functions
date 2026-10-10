import random

secret_number = random.randint(1, 100)
999attempts = 0

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low")

    elif guess > secret_number:
        print("Too High")

    else:
        print("Correct!")
        print("Attempts taken:", attempts)
        break

