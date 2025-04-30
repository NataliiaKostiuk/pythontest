# A door unlocks only if a person has the correct PIN code (1234) and is an authorised user.
# Write a program that asks for the PIN and if the user is authorised (True/False) 
# and then checks if the door should unlock.
# Example output:
# Enter PIN: 1234
# Are you authorised? (True/False): True
# Door unlocked: 

pin = input("Enter your PIN code: ")
isAuthorised = input("Are you authorised? (True/False): ")

access = True if pin == "1234" and isAuthorised.lower() == "true" else False
print(access)
if access:
    print("Door unlocked! Welcome!")
else:
    print("Enter correct PIN code or authorize!")    