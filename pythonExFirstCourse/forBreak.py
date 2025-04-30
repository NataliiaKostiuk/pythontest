#FOR/BREAK example 


for x in range(4): #using FOR to run the program up to 4 times

  #input is used to collect data from user
  username=input("Please enter your username: ")
  
  pwd=input("Please enter your password: ")
  
  if (pwd == "glasgow" and username=="maks"): #using IF and == boolean to determine what to do if data is true
    print("Welcome",username)
    break #using break to stop FOR loop once conditions have been met

  else: #using else to print message if conditions arent met
    print("Incorrect password/username! ", x+1) # adds +1 tries to the loop
    print("goodbye")