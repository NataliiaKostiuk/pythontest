import string



def passwordCheck(password):
    upperCount = 0
    lowerCount = 0
    digitCount = 0
    symbolCount = 0
    charCount = 0
    upperChar = string.ascii_uppercase
    lowerChar = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    if len(password) > 6:
        charCount +=1
        print(charCount)
    else:
        print("Your password has to be more then 6 symbols")
        return
    for char in password:
        if char in upperChar:
            upperCount +=1
            print(f"Upper {upperCount}")
        elif char in lowerChar:
            lowerCount +=1
            print(f"Low {lowerCount}")
        elif char in digits:
            digitCount +=1
            print(f"Digits {digitCount}")
        elif char in symbols:
            symbolCount +=1
            print(f"Symbol {symbolCount}")
        else:
            print("Try again! ") 
    if upperCount and lowerCount and charCount and  digitCount and symbolCount:
        print("Password is strong. Your password meets the minimum requirements.") 
    else:
        print("Your password is weak! Password has to include at least 1 capital letter and 1 symbol.")                      


print("Welcome to the Password Strength Checker!\n")
password = input("Enter your password: ")

passwordCheck(password)

