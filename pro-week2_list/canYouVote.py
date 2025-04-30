# Write a program that asks the user for their age and
#  whether they are a citizen (True or False). The program should check if
# they are eligible to vote (must be 18 or older and a citizen).
# Example output:
# Enter your age: 20
# Are you a citizen? (True/False): True
# Can you vote? True

age = int(input("Enter your age: "))
isCitizen = input("Are you a citizen? (True/False): ")

isVote = True if age >= 20 and isCitizen.lower() == "true" else False
print(isVote)
if isVote:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")    