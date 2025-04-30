# Create a new program that has the following functions and Algorithm
# GetName
# This function will return the name of the user
# GetAge
# This function will return the age of the user
# Algorithm
# Get Name from User
# Get Age from user
# IF age >=18 welcome user using Name
# Else
# Tell user they are too young using Name
# ENDIF

# def getName():
#     return str(input("Enter your name  "))
# def getAge():
#     return int(input("Enter your age:  "))
# def getAddress():
#     return str(input("Enter your address:  "))

def getOptions(option):
    return input(f"Enter your {option}: ")


def checkAge():
    name = str(getOptions("name"))
    age  = int(getOptions("age"))
    if age >= 21:
        print("Hello", name)
        address = str(getOptions("address"),name)
        print(f"Your address is {address}")
    else:
        print(f"Sorry {name}. You are too young...") 
        
           
checkAge()        