def read_hours():
# we give the file a name and use it to reference the file throughout the code
# the file is being opened for reading
    testFile = open("hours.txt","r") 
# we open up the file we created to read the contents
    for line in testFile:#for each line in text file do the following  
        stripped_line = line.strip()#read in all characters as string
        hours.append(stripped_line)#Add into the data list 
    testFile.close()
# close the file

def read_rate():
# we give the file a name and use it to reference the file throughout the code
# the file is being opened for reading
    testFile = open("rate.txt","r") 
# we open up the file we created to read the contents
    for line in testFile:#for each line in text file do the following  
        stripped_line = line.strip()#read in all characters as string
        rate.append(stripped_line)#Add into the data list 
    testFile.close()
# close the file

def read_name():
# we give the file a name and use it to reference the file throughout the code
# the file is being opened for reading
    testFile = open("name.txt","r") 
# we open up the file we created to read the contents
    for line in testFile:#for each line in text file do the following  
        stripped_line = line.strip()#read in all characters as string
        name.append(stripped_line)#Add into the data list 
    testFile.close()
# close the file

def calc_wages():
  for x in range(len(name)):
    wage = float(rate[x]) * float(hours[x])
    print("\n", name[x], " wages are £ ",round(wage,2))
  

rate=[] # set a blank list for the file data rate
hours=[] # set a blank list for the file data hours
name=[] # set a blank list for the file data name
# main code
print("Read from the files ")
print()
read_hours()
read_rate()
read_name()
print()
calc_wages()