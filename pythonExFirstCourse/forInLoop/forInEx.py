################################### more than #################
# marks = [79,45,51,34,90,99]
# count = 0
# for i in range(len(marks)):
#     if int(marks[i]) < 50:
#         count = count + 1
# print("Total marks  under 50 is ", count)   

############################## max ##############################
# max = marks[0]
# for i in range(len(marks)):
#     if int(marks[i])> max:
#         max = marks[i]
# print("Highest score is ", max)  
# ########################## min ################      
# marks = [79,45,51,34,90,99]

# for i in range(len(marks)):
#     if int(marks[i])< min:
#         min = marks[i]
# print("Highest score is ", min)     

############ total####################
marks = [79,45,51,34,90,99]
total = 0
for i in range(len(marks)):
    total = total + marks[i]
    average = total/len(marks)
print("Average is ", round(average,2) ) 