import random

print("Welcome to Guess The Number!")
print("Guess The Number 1 to 100")
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Gimme your guess (1-100): "))
    except ValueError:
        print("Numbers only!")
        continue

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! The number is ", number)
        break
