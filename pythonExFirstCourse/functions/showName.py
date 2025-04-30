# def getName():
#     return input("Enter your name :")
# print("User's name is ",getName())


# ##################################################################
# def getHours():
#     hours = float(input("Please enter your hours:  "))
#     return hours
# def getRate():
#     rate = float(input("Please enter your rate:  "))
#     return rate
# workHours = getHours()
# workRate = getRate()
# print("Wages this week are",getRate()*getHours())   

#####################################################################################
# def GetLenName(name):
#     print(len(name))     

# def getName():
#     return input("Enter your full name:  ")
# GetLenName(getName())

#######################################################################################

def getNumber(options):
    return float(input(f"Enter {options}"))


wage = (getNumber("rate")*getNumber("hours"))
print("Your wage is", wage)

######################################################################################