import random
secret = "Nataliia"
print(len(secret))
length = len(secret)
print(length)
ramdomNumber = random.randint(1, length)
print(ramdomNumber)
numOfPassword = input(f"Press {ramdomNumber} symbol of your password: ")
print(numOfPassword)
if(numOfPassword==secret[ramdomNumber]):
    print("Logged in now")
else:
    print("You are locked out now !")    