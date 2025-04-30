string = 'Hello'
reversedString = string[::-1]
print(reversedString)


sameReversedString = ''.join(reversed(string))
# sameReversedString = reversed(string)#['o', 'l', 'l', 'e', 'H']
print(sameReversedString)

for letterOfString in reversed(string):
    print(letterOfString, end='')