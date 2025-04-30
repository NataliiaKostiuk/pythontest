# Write a program that asks the user to enter an email address so they 
# can be added to a mailing list 

# Check if the email address is valid by checking it contains an @ 

# If it doesn't have an @ give them 3 attempts to re-enter the email. 

# If it's a valid email address display a "You have been added to our mailing list"
 

attempt = 0
while  attempt !=3:
    email = input("Enter your email address : ")
    attempt =attempt+1
    validEmail = email.find("@")
    print(validEmail)
    if validEmail == -1:
        print("Your email address id invalid. Try againg?")
        print(f"{3 - attempt} attempts left")
  
    else:
        print("You have been added to our mailing list")  
        break  
