# Set the variable ‘choice’ to 0
# Set program the code to run while the choice is not equal to 5
# Print out a menu showing the options the user has
# Obtain the user’s choice
# If user chooses option 1,
# Obtain the two numbers the user wants to add together
# Add the first number to the second number
# Print the result
# If user chooses option 2,
# Obtain two numbers from the user
# Subtract the first number from the second number
# Print the result
# If user chooses option 3,
# Obtain two numbers
# Multiply the two numbers
# Print the result
# If user chooses option 4,
# Obtain two numbers
# Divide the first number by the second number
# Print the result
# If user chooses option 5,
# Exit the program
# Print ‘Goodbye’
# If any other choice is made, print ‘Incorrect Value’

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Devision by 0 impossible."

def menu():
    print("Choose the option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplycation")
    print("4. Devision")
    print("5. Exit")
    

choice = 0
a = int(input("Input you first number : "))
b = int(input("Input you second number : "))
while choice != 5:
   menu()
   choice = int(input("Enter number of option (1-5): "))
   if choice == 1:
      result = add(a,b)
      print(f"Resalt is {result}")
   elif choice == 2:
      result = subtract(a,b)
      print(f"Resalt is {result}")
   elif choice == 3:
      result = multiply(a,b)
      print(f"Resalt is {result}")
   elif  choice == 4:
      result = divide(a,b)
      print(f"Resalt is {result}")
   elif choice == 5:
       print("Good bay!!")
       break
   else:
       print("Incorrect Value")                
    
     