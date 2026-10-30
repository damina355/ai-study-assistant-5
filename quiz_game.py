# Quiz Game

score = 0

print("Welcome to the Python Quiz!")

answer = input("1. What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What is 5 + 7? ")

if answer == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. What programming language are you learning? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()
print("Your final score is:", score, "/ 3")