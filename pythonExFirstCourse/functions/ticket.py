
correctPasword = "password"

def calculate(ticketPrice,quantity):
    amount = ticketPrice*quantity
    return amount

def display_menu():
    print("Menu:")
    print("1. Adult ticket")
    print("2. Children ticket")
    print("3. Student ticket")
    print("4. OAP ticket")
    print("5. Exit")

attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == correctPasword:
        print("Welcome!")
        while True:
            display_menu()
            choice = int(input("Choose the option (1-5): "))
            if choice == 1:
                print(choice)
                ticketPrice = 10
                quantity = int(input("Enter quantity of tickets :"))
                result = calculate(ticketPrice,quantity)
                print(f"The price of {quantity} Adult tickets is {result}")
            elif choice == 2:
                ticketPrice = 5
                quantity = int(input("Enter quantity of tickets :"))
                result = calculate(ticketPrice,quantity)
                print(f"The price of {quantity} Children tickets is {result}")
            elif choice == 3:
                ticketPrice = 7
                quantity = int(input("Enter quantity of tickets :"))
                result = calculate(ticketPrice,quantity)
                print(f"The price of {quantity} Student tickets is {result}")
            elif choice == 4:
                ticketPrice = 5
                quantity = int(input("Enter quantity of tickets :"))
                result = calculate(ticketPrice,quantity)
                print(f"The price of{quantity} OAP tickets is {result}")
            elif choice == 5:
                print("Good bay!")
                break
            else:
                print("Incorrect choice! Choose the option between 1 and 5.")
    else:
        attempts += 1
        print(f"Incorrect password: {3 - attempts} attempts left!")
    if attempts == 3:
        print("Numbers of attempts are exceeded. Access is denied.")

