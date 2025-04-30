
from handler import getName, getAge


def listOfFruit():
    listFruit = []
    print("Enter your favourite fruit:")
    for i in range(3):
        fruit = input()
        listFruit.append(fruit) 
    return listFruit

def main():
    name = getName()
    print(f"Hello {name}")
    age = getAge()
    if age >= 18:
        print("You are adult!")
    fruitList = listOfFruit()
    for i in fruitList:
        print(f"Your favorite fruit is {i}")

main()
     



