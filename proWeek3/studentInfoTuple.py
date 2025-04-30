from handler import getAge, getName

def getStudentGrade():
    grade = int(input("Enter students grade: "))
    return grade

def searchStudent(studentList):
    while True:
        studentName = input("Enter the student's name please ")
        for student in studentList:
            if student.lower() == studentName.lower():
                print(f"Student found!\nName: {student[0]}\nAge: {student[1]}\nGrade: {student[2]}")
            else:
                print("Sorry, student not found.")
        choice = input("Would you like to try again? YES/NO: ")
        if choice.lower() != 'no':
            print("Goodbye!")
            break 

def displayStudentList():
    if studentList:
        print("\nList of all students:")
        for student in studentList:
            print(f"Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")
    else:
        print("The student list is empty.")


def deleteStudent(studentList):
    while True:
        studentName = input("Enter the name of the student you want to delete: ")
        for student in studentList:
            if student.lower() == studentName.lower():
                studentList.remove(student)
                print(f"\nStudent {student[0]} has been successfully deleted!")
            else:
                print("\n Student not found. Nothing was deleted.")

        choice = input("\nWould you like to delete another student? YES/NO: ")
        if choice.lower() != 'no':
            print(" Goodbye! ")
            break

def updateStudent(studentList):
    while True:
        studentName = input("Enter the name of the student you want to update: ")
        found = False
        for i, student in enumerate(studentList):
            if student[0].lower() == studentName.lower():
                print(f"Updating student {student[0]}")
                new_name = getName()
                new_age = getAge()
                new_grade = getStudentGrade()
                studentList[i] = (new_name, new_age, new_grade)
                print(f"Student {studentName} has been updated successfully!")
                found = True
                break
        if not found:
            print("\nStudent not found. Nothing was updated.")

        choice = input("\nWould you like to update another student? YES/NO: ")
        if choice.lower() != 'yes':
            print("Goodbye!")
            break


def menu():
    print("""
   Please choose options:       
   1. Add a new student's information.
   2. Display the list of all students and their information.
   3. Search for a student by name and display their information.
   4. Update a student's information.
   5. Delete a student's information.
   6. Exit the program.
    """)

studentList = []

def createStudentList():
    while True:
        choice = input("Do you want to add a student's information? YES/NO: ")
        if choice.lower() == 'yes':
            student = (getName(), getAge(), getStudentGrade())
            studentList.append(student)
        elif choice.lower() == 'no':
            print("Student's list is completed")
            break
        else:
            print("Please enter YES or NO!")

def main():
    while True:
        choice = menu()
        if choice == '1':
            createStudentList()
        elif choice == '2':
            displayStudentList()
        elif choice == '3':
            searchStudent(studentList)
        elif choice == '4':
            updateStudent(studentList)
        elif choice == '5':
            deleteStudent(studentList)
        elif choice == '6':
            print("Goodbye! 👋")
            break
        else:
            print("Please choose a correct option between 1 and 6.")

# main()





