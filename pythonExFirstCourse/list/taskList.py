# Create InfoList =[33,4,"Hello",3.14,"Sunshine"]
# While choice is not 5
# Show Menu
# Get Choice 
# if choice is 1
# Show list
# Else If choice is 2
# Append to list
# Else if choice is 3
# Insert into list
# Else if choice is 4
# Show Length of list
# Else if choice is 5
# Display exit message
# else tell user they entered wrong choice
# END ELIF
# END WHILE

def menu():
    print("""
List manipulations
1. Show list
2. Append to list
3. insert to list
4. Show length list
5. Exit                              
                              """)
def appendList():
    value = input("Choose the value, which you want to append: ") 
    return value 
  
def choosePosition():
    return int(input("Choose position:  "))
infoList =[33,4,"Hello",3.14,"Sunshine"]  
choice = 0 
while True:
    menu()
    choice= int(input("Choose your potion (1-5): "))
    if choice == 1:
        print(infoList)
    elif choice == 2:
        infoList.append(appendList())
        print(infoList)
    elif choice == 3:
        infoList.insert(choosePosition(), appendList())
        print(infoList)
    elif choice == 4:
        print(f"Length of list is {len(infoList)}")  
    elif choice == 5:
        print("Goodbay!!!")
        break
    else:
        print("Incorrect option. Try againg!!")            


