def Additon(num1, num2):
    sum = num1 + num2
    return sum

def Subtraction(num1, num2):
    sub = num1-num2
    return sub

def Multyplication(num1,num2):
    res = num1 * num2
    return res

def Divission(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero.")
    return num1 / num2

def getName():
    name = input("Enter your name:  ")
    while name == '':
       name = input("You have to enter you name here: ")
       if name != "":
           break
    return name

def getAge():
    age = input("Enter your age: ")
    while not age.isdigit():
        print("Enter your age: ")
    age = int(age)
    return age   