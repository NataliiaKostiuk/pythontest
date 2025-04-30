

correctPasword = "password"
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == correctPasword:
        studentName = str(input("Enter you name "))
        print("Welcome", studentName)
        while True:
            mark = int(input("Enter your mark "))
            if mark >= 70:
                print(f"Congratulation {studentName}! You got an A")
            elif mark < 70 and mark >=60:
                print(f"Congratulation {studentName}! You got an B")
            elif mark < 60 and mark >=50:
                print(f"Congratulation {studentName}! You got an C")
            else:
                print(f"Bad news {studentName} You are failed exam")
            answer = str(input("Would you like check your mark againg? ")).lower().strip()
            if answer == "no":
               print("Good bay!")
               break        
    else:
        attempts += 1
        print(f"Incorrect password: {3 - attempts} attempts left!")
    if attempts == 3:
        print("Numbers of attempts are exceeded. Access is denied.")