# Alter your program so that it will read the name, coursework mark and prelim mark
# for all the 15 students in your class from an external file (available from your
# assessor).
# Make sure that you add internal commentary to explain how the file operation works and its
# purpose.
# Task 7:
# • Alter your program to enable it to find out how many “A” passes are in the class by
# using the “Count Occurrences” standard algorithm.
# Use internal commentary to describe how the “Count Occurrences” algorithm works.
# • Alter your program to find out who has the best percentage in the class by using the
# “Find Max” standard algorithm.
# Use internal commentary to describe how the “Finding Max” algorithm works.
# Step 8:
# Explain how the computer processes the program using the fetch-execute cycle with
# reference to processor, memory and buses.
# Note: You must use the assessment report to record your evidence and submit the


# Initialize lists to store student data
scoreList = []  # Stores final scores of students
gradeList = []  # Stores grades of students
studentNames = []  # Stores names of students
courseMarks = []  # Stores course marks 
prelimMarks = []  # Stores preliminary marks 
failedStudents = []  # Stores names of students who failed the exam

# Function to read student names from 'names.txt' and store them in studentNames list
def GetStudentNames():
    file = open("names.txt", "r")  # Open the file in read mode
    for line in file:
        strippedLine = line.strip()  # Remove extra spaces and newline characters
        studentNames.append(strippedLine)  # Append name to the studentNames list
    file.close()  # Close the file
    return studentNames  # Return the list of names


# Function to read course marks from 'mark1.txt' and store them in courseMarks list
def GetCourseMarks():
    file = open("mark1.txt", "r")  # Open the file in read mode
    for line in file:
        strippedLine = line.strip()  # Remove extra spaces and newline characters
        courseMarks.append(strippedLine)  # Append mark to the courseMarks list
    file.close()  # Close the file


# Function to read preliminary marks from 'mark2.txt' and store them in prelimMarks list
def GetPrelimMarks():
    file = open("mark2.txt", "r")  # Open the file in read mode
    for line in file:
        strippedLine = line.strip()  # Remove extra spaces and newline characters
        prelimMarks.append(strippedLine)  # Append mark to the prelimMarks list
    file.close()  # Close the file


# Function to calculate final scores and store them in scoreList
def CountScores():
    for i in range(len(courseMarks)):  # Loop through all students
        # Convert marks to float, compute total percentage and round to 2 decimal places
        result = ((float(courseMarks[i]) + float(prelimMarks[i])) * 100 / 150)
        scoreList.append(round(result, 2))  # Append calculated score to scoreList
    return scoreList  # Return the final scores


# Function to assign letter grades based on the computed scores
def CountGrades():
    grade = ''  # Initialize grade variable
    for i in range(len(scoreList)):  # Loop through all students
        if scoreList[i] >= 70:
            grade = "A"  # Assign grade 'A'
            gradeList.append(grade)
        elif scoreList[i] >= 60 and scoreList[i] < 70:
            grade = "B"  # Assign grade 'B'
            gradeList.append(grade)            
        elif scoreList[i] >= 50 and scoreList[i] < 60:
            grade = "C"  # Assign grade 'C'
            gradeList.append(grade)            
        elif scoreList[i] >= 45:
            grade = "D"  # Assign grade 'D'
            gradeList.append(grade)            
        else:
            grade = 'F'
            gradeList.append(grade) # Assign grade 'F'
            failedStudents.append(studentNames[i])  # Add student to failed list
    return gradeList  # Return the list of grades


# Function to find the student with the highest score
def MaxScore(scoreList):
    maxScore = scoreList[0]  # Assume the first score is the highest
    maxIndex = 0  # Store index of the highest score
    for i in range(len(scoreList)):  # Loop through all students
        if scoreList[i] > maxScore:
            maxScore = scoreList[i]  # Update maxScore
            maxIndex = i  # Update index of the highest-scoring student
    return print(f"{studentNames[maxIndex]} received the highest score {maxScore}")  # Print the result


# Function to count the number of students who received an 'A' grade
def NumberOfALevel(gradeList):
    count = 0  # Initialize counter
    for i in range(len(gradeList)):  # Loop through all students
        if gradeList[i] == 'A':  # Check if the grade is 'A'
            count += 1  # Increment counter
    return count  # Return the number of students with 'A' grades

# Function to display students who failed the exam
def ShowFailedStudents():
    # Check if there are any failed students in the list
    if failedStudents:
        print("Students who failed the exam:")  # Print the text
        for student in failedStudents:  # Loop through the list of failed students
            print(student)  # Print each student's name
    else:
        print("No students failed the exam!")  # Print message if no one failed


# Function to display the menu options
def Menu():
    print("""
Welcome! Choose the option:
          1: Read student names
          2: Student who failed exam
          3: Count the number of students who received an 'A' grade
          4: Show the student who received the highest grade
          5: Exit
    """)


# Function to execute the main program logic
def ShowResults():
    GetStudentNames()  # Read student names from file
    GetCourseMarks()  # Read course marks from file
    GetPrelimMarks()  # Read preliminary marks from file
    CountScores()  # Calculate final scores
    CountGrades()  # Assign grades  
    while True:  # Infinite loop to keep showing the menu until the user exits
        Menu()  # Display menu
        choice = int(input("Enter your choice: "))  # Get user input
        if choice == 1:
            print(studentNames)  # Print the list of student names
        elif choice == 2:
           ShowFailedStudents()         
        elif choice == 3:
            numberOfStudent = NumberOfALevel(gradeList)  # Count students with 'A'
            print(f"{numberOfStudent} students received 'A' level")  # Display result
        elif choice == 4:
            MaxScore(scoreList)  # Find and display the highest score            
        elif choice == 5:
            print("Goodbye!")  # Exit the program
            break  # Break out of the loop
        else:
            print("Choose the correct option!")  # Handle invalid input


# Run the program
ShowResults()