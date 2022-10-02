import random
number = random.randint(1,100)
userGuess = None
guesses = 0

while (userGuess != number):
    userGuess = int(input("Enter your guess: "))
    guesses += 1

    if (userGuess == number):
        print(f"Congrats! Your guess is correct. The number was {number}")
    else:
        if (userGuess < number):
            print("Try Again! Higher please.")
        else:
            print('Try Again! Lower!.')







