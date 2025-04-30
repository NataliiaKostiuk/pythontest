
# Your task is to complete the following challenges:
# Create a list of students first names, minimum of 10.
# Print the original list of student names.
# Slice the list to get the first 5 names and print them.
# Slice the list to get the last 3 names and print them.
# Get the size of the list and print it.
# Add a new student name, "Kate", to the end of the list and print the updated list.
# Insert a new student name, "Liam", at index 3 and print the updated list.
# Iterate through the list and print each student name.

students = ["Alex", "Sarah", "Daniel", "Emily", "Michael", "Sophia", "James", "Olivia", "Ethan", "Isabella"]
print(students)
firstNameList = students[: 5]
print(firstNameList)
lastNameList = students[7:]
print(lastNameList)
print(len(students))
students.append("Kate")
print(students)
students.insert(3, "Liam")
print(students)
for student in students:
    print(student)


