string = input("Enter your string: ")
vowels = 'aeiouAEIOU'
volwesList= []
for char in string:
    if char in vowels:
        volwesList.append(char)
print(volwesList)

