# Leap Year Checker
# Write a Python function that takes a year as input and returns True if it is a leap year, and False otherwise.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
      
def CheckLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False   

year = int(input("Enter the year: "))  # Convert input to integer
if CheckLeapYear(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")