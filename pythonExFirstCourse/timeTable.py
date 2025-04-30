import random

randomNumber = random.randint(1, 10)
chosenTable = int(input("Which times table would you like to practice? (1-10): "))
print(f"What is {randomNumber} x {chosenTable}?")
userGuess = int(input("Your guess: "))
correctAnswer = randomNumber * chosenTable

if userGuess == correctAnswer:
    print("Well done! That's correct.")
else:
    print("Incorrect. The correct answer is {correct_answer}.")