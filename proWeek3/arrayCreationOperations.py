import array

myArray = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(myArray)
print(len(myArray))

sum = 0
for i in myArray:
    sum = sum + i
print(sum)    

