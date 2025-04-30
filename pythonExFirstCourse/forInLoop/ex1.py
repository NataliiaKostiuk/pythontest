# Create new list called Marks = [20,78,50,52,12,34,88,90,3,52]
# WHILE choice is not 6
# Display Menu
# Get choice
# IF choice is 1
# Display the full list
# ELSE IF choice is 2
# Find & print Highest Value 
# ELSE IF choice is 3
# Find and print Lowest Value
# ELSE IF choice is 4
# Count then print the number of values under 50
# ELSE IF choice is 5
# Get value from user
# IF value is <0 or value >100
# print error message, value out of range
# ELSE
# Append Value to end of list
# END IF
# ELSE IF choice is 6
# Print Exit Message
# ELSE Print error message
# END ELIF
# END WHILE

marks = [20,78,50,52,12,34,88,90,3,52]

def menu():
    print("""
1. Show full list
2. Show higher value
3. Show lower value
4. Count numers under 50
5. Append value
6. Exit                                                  
          
""")
def handleHigherValue(list):
    max = list[0]
    for i in range(len(list)):
       if int(list[i])> max:
          max = list[i]
    return print("Highest value is ", max)  

def handleLowerValue(list):
    min = list[0]
    for i in range(len(list)):
      if int(list[i]) < min:
        min = list[i]
    return print("Lower value is ", min) 

def handleNumberUnder(list):
   counter = 0
   for i in range(len(list)):  
      if int(list[i]) < 50:  # Исправлено на < 50
         counter += 1  
   print("The number of values under 50 is", counter)  # Убрали return

def AppendValue(list):
   value = int(input("Choose the number, which you want to append: "))
   if value < 0 or value > 100:
      print("Enter a number between 0 and 100 ")  # Исправлен текст ошибки
   else:
      list.append(value)  # Исправлено
      print(f"{value} appended in list {list}")  # Выводим актуальный список


while True:
    menu()
    choice =int(input("Choose the option "))
    if choice == 1:
       print("This is full list",marks)
    elif choice == 2:
       handleHigherValue(marks)
    elif choice == 3:
       handleLowerValue(marks)  
    elif choice == 4:
       handleNumberUnder(marks)
    elif choice == 5:
       AppendValue(marks)
    elif choice == 6:
       print("Goodbay!!!")
       break
    else:
       print("Choose correct option") 
   

          
         
   