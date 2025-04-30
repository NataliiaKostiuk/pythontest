# Write a program that asks the user for a number and checks
#  if it is between 10 and 50 (inclusive) using logical operators.
# Example output:
# Enter a number: 25
# Is the number between 10 and 50? True
 
number = int(input("Enter the number:  "))

if number>= 10 and number <= 50:
    print(f"{number} is between 10 and 50")
else:
    print(f"{number}  is not between 10 and 50")    