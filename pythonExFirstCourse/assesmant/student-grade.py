
def Validation(courseMark, prelimMark):   #Function for validation
    if courseMark > 60 or prelimMark > 90:    #Checks that marks are within acceptable limits
        return False  # Return False if data is incorrect
    return True    # Return True if data is correct

def CountPercentage(courseMark, prelimMark):   #Function for counting percentage
    result = float(((courseMark + prelimMark) * 100) / 150)
    return result  #Return average score

def menu():   # Function for showing menu
    print("""
    Welcome! Check your grade:
    1 - Start
    2 - Exit
    """)

def ShowGrade():  # Main function to handle user interaction and grading
    while True:   # Infinite loop to keep the program running until the user chooses to exit     
        menu()    # Display the menu options
        choice = int(input("Enter your choice: "))  # Get user's choice
        if choice == 2:   # If the user chooses to exit
            print("Thanks for using our service. Goodbye!")
            break  # Exit the main loop and terminate the program
        elif choice != 1:   # If the user enters an invalid option
            print("Try again! Please enter 1 or 2.")
            continue     # Restart the loop to show the menu again    
        while True:      # Loop to ensure valid marks are entered
            courseMark = int(input("Enter your coursework mark (0-60): "))   # Get coursework mark
            prelimMark = int(input("Enter your prelim mark (0-90): "))     # Get prelim mark
            if not Validation(courseMark, prelimMark):    # Calling validation function
                print("Invalid mark! Please enter values within the correct range.")
                continue             # If invalid, ask the user to enter marks again
            percentage = CountPercentage(courseMark, prelimMark)  # Calculate the percentage
            print(f"Your percentage is {round(percentage, 2)}%")  # Display the percentage
            if percentage >= 70:              # Determine and display the grade based on the percentage
                print("Excellent! Your grade is A")
            elif percentage >= 60:
                print("Congratulations! Your grade is B")
            elif percentage >= 50:
                print("Well done! Your grade is C")
            elif percentage >= 45:
                print("Your grade is D")
            else:
                print("You fail")

            break  # Exit the inner loop and return to the main menu
ShowGrade()