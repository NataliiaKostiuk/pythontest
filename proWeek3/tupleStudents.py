students = [
    ("Alice", 20, 85),
    ("Bob", 21, 90),
    ("Charlie", 19, 78),
    ("Diana", 22, 95),
    ("Eve", 20, 82)
]

firstStudent = students[0]
name, age, score = firstStudent
newStudent = ("Anna", 21, 87)
updateStudents = students + [newStudent]
def getEveryStudent(updateStudent):
    for student in updateStudent:
        name, age, grade = student
        print(f"{name} is {age} year old. Student's grade is {grade}")

getEveryStudent(updateStudents)        