# Creating a dictionary to store student information
student_dict = {
    101: {'name': 'Alice', 'grade': 'A'},
    102: {'name': 'Bob', 'grade': 'B'},
    103: {'name': 'Charlie', 'grade': 'C'},
    104: {'name': 'David', 'grade': 'A'},
    105: {'name': 'Eve', 'grade': 'B'}
}

# Accessing values in the dictionary
print("Name of student with ID 103:", student_dict[103]['name'])  # Output: Charlie
print("Grade of student with ID 104:", student_dict[104]['grade'])  # Output: A

# Adding a new student
student_dict[106] = {'name': 'Frank', 'grade': 'B'}

# Updating grade of an existing student
student_dict[101]['grade'] = 'B'

# Deleting a student
del student_dict[105]

# Checking if a student exists
if 102 in student_dict:
    print("Student with ID 102 exists.")
else:
    print("Student with ID 102 does not exist.")

# Iterating over the dictionary
print("Student IDs and Names:")
for student_id, info in student_dict.items():
    print(f"ID: {student_id}, Name: {info['name']}, Grade: {info['grade']}")

# Getting the number of students
num_students = len(student_dict)
print("Number of students:", num_students)