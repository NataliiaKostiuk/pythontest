# marks =[ 23, 45, 27, 58, 67]
# name =["Joanna","Hanna", "Nataliia", "Jany","Alex"]
# max = marks[0]
# for i in range(len(marks)):
#     print(i)
#     if int(marks[i])> max:
#         print(i)
#         max = marks[i]
#         print(max)
#         position = i
# print(f"Highest score from {name[position]}is {max}")   
############################### ##################################
# hour= [ 23, 56, 17, 34]
# rate = [23.2, 17.5, 15.5,45.67]
# name =["Joanna","Hanna", "Nataliia", "Jany"]
# for i in range(len(rate)):
#     print(name[i], "your wage is", round(int(hour[i])* float(rate[i])))
########################################################################################
hour= [ 23, 56, 17, 34]
rate = [23.2, 17.5, 15.5,45.67]
name =["Joanna","Hanna", "Nataliia", "Jany"]
wage = []
for i in range(len(rate)):
    wage.append(int(hour[i])*float(rate[i]))
    print(name[i], "your wage is", round(wage[i],2))
     