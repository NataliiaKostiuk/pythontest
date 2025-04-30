
my_list = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed_list = [1, "hello", True, 3.14]
arr = [] #False
num = None #False
integer = 0 #False
dictionary = {} #False
print( integer == True)
# Accessing elements
print(my_list[0])   # Output: 1
print(names[2])     # Output: Charlie
print(mixed_list[-1]) # Output: 3.14

# Slicing
print(my_list[1:4])   # Output: [2, 3, 4]
print(names[:2])      # Output: ['Alice', 'Bob']
print(mixed_list[2:]) # Output: [True, 3.14]


# Modifying elements
my_list[0] = 10         # Changing the first element
names.append("David")   # Adding an element to the end
mixed_list.remove(True) # Removing an element
names.insert(1, "Eve")
popped_element = my_list.pop(2)


length = len(my_list)
index = names.index("Charlie")
count = mixed_list.count(3.14)


my_list = ['apple', 'banana', 'orange']

for index, fruit in enumerate(my_list, start=1):
    print(f"Item {index}: {fruit}")