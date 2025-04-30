# Write a program that asks the user for a day of the week and checks if it’s the weekend (Saturday or Sunday).

# Example output:
# Enter a day of the week: Saturday
# Is it the weekend? True

day = input("Enter day: ")

weekend = True if day.lower() == "saturday" or day.lower() == "sunday" else False
print(weekend)
if weekend:
    print(f"{day} is  a weekend")
else:
    print(f"{day} is not a weekend")    