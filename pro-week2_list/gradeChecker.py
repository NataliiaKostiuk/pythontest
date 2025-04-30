# You are given a list of student scores. Your task is to check each score and 
# whether it's a passing grade or a failing grade. A passing grade is any score greater
# than or equal to 60, while a failing grade is any score less than 60.
# Your task is to:

# Create a list named student_scores containing the following scores: 70, 45, 85, 30, 65.
# Iterate through each score in the student_scores list.
# For each score, use the ternary operator to print "Pass" if the score is greater than or equal to 60, and "Fail" otherwise.

studentScore =[70, 45, 85, 30, 65]

# passedStudent = [student for student in studentScore if student >= 60]
# print(passedStudent)
# print(f"{len(passedStudent)} students passed exam!")

for score in studentScore:
    print("Pass" if score >= 60 else "Fail")
  



