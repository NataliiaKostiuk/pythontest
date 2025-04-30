# Logical Operator Exercise - Eligibility Checker

# Instructions

# You are tasked with creating a program to check whether a person is eligible to vote and drive based 
# on their age and citizenship. The eligibility criteria are as follows:#

# To vote, a person must be at least 18 years old and a citizen.
# To drive, a person must be at least 16 years old and a citizen.
# Your task is to:

# Prompt the user to enter their age and citizenship status (as "citizen" or "non-citizen").
# Check if the person is eligible to vote and drive based on the provided age and citizenship status.
# Print appropriate messages indicating whether the person is eligible to vote and drive or not.

age = int(input("Enter your age: "))
isCitizen = input("Are you a citizen? (True/False): ")

if age >= 18 and isCitizen.lower() == "true":
    print("You can vote")
else:
    print("You must be at least 18 years old and a citizen")

if age>= 16 and isCitizen.lower() == "true":
    print("You can drive") 
else:
    print("You must be at least 16 years old and a citizen")           


   