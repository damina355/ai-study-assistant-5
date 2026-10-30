# Guess the Number Game

secret_number = 7

guess = int(input("Guess the number (1-10): "))

while guess != secret_number:
    print("Wrong! Try again.")
    guess = int(input("Guess the number (1-10): "))

print("Congratulations! You guessed the number!")