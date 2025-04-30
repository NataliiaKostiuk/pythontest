import string
print(string.ascii_letters)
print(string.digits)

specialCharacters = string.punctuation

counter = 0

messsage = 'Hello, World'
for char in messsage:
    if char in specialCharacters:
        counter +=1
print(counter)        