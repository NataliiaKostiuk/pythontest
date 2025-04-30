from handler import Additon, Subtraction, Multyplication, Divission, getName


def menu():
    print("""       
Press:
1. Addition
2. Subtraction
3. Multyplication
4. Divission 
5. Exit                                                 
""")

def getNumbers():
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        if num1.lstrip('-').isdigit() and num2.lstrip('-').isdigit():   #allows negative numbers
            return int(num1), int(num2)
            break
        else:
            print("Invalid input. Please enter whole numbers (can be negative).")


def main():
    name = getName()
    print(f"Hello {name}! Let's do some maths ") 
    turpleName = getNumbers()
    num1, num2 = turpleName 
    result = 0
    while True:
        menu()
        option = input("Choose the option:   ")
        if option == "1":
           result = Additon(num1, num2)
           print(result)
        elif option == "2":
           result = Subtraction(num1, num2)
           print(result)    
        elif option == "3":
           result = Multyplication( num1, num2)
           print(result)
        elif option == "4":
           result = Divission(num1, num2)
           print(result)
        elif option == "5":
           print("Thank you for visiting our website!")
           break
        else:
           print("Choose the correct options")                

main()