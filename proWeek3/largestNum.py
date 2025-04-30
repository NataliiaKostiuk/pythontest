def getNumbers():
    listNumbers = []
    for i in range(3):
        while True:
            num = input(f"Enter number {i + 1}: ")
            if not num.isdigit():
                print("You have to enter just number!")
            else:
                num = int(num)
                listNumbers.append(num)
                break
    return listNumbers   

def main():
    numList = getNumbers()
    largestNumber = max(numList)
    print(largestNumber)

main()    

