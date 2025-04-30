import random
number = random.randint(1,100)
userName = input("Enter your name please ")
print(userName)
position = userName.find(" ")
print(userName[0]+userName[position+1] + str(number))