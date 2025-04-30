# Create a program that asks the user to enter their first name.

# If the length of the name entered is less than 3 ask them to enter their name again.

# They are allowed 3 attempts and will get a Welcome message using their name if they enter long enough username

chance = 0
while chance !=3:
    chance = chance+1
    user_name = input(" Enter your first name  ")
    if len(user_name) >= 3:
        print(f"Welcome {user_name}")
        break
    else:
        print("Your name has being more then 3 characters! Try againg")
        print(f"{3 - chance} chances left")
