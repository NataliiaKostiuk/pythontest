

def read_hours():

    testFile = open("hours.txt","r") 
    for line in testFile:
        stripped_line = line.strip()
        hours.append(stripped_line)
        print(hours)
    testFile.close()
    return hours


def read_rate():
    testFile = open("rate.txt","r") 
    for line in testFile: 
        stripped_line = line.strip()
        rate.append(stripped_line)
    testFile.close()
    return rate


def read_name():
    testFile = open("name.txt","r") 
    for line in testFile: 
        stripped_line = line.strip()
        name.append(stripped_line)
    testFile.close()
    return name


def calc_wages():
  for x in range(len(name)):
    wage.append(float(rate[x])*float(hours[x]))
    

def print_wages():
  for x in range(len(name)):
    print("\n", name[x], " wages are £ ",round(wage[x],2))

    
def get_max():
  max =wage[0] 
  for x in range(len(name)):
    if (max < wage[x]):
      max = wage[x]
  print (" MAx wage is £ ",max)
  


def get_min():
  min =wage[0] 
  for x in range(len(name)):
    if (min > wage[x]):
      min = wage[x]
  print (" Min wage is £ ",min)

def wage100():
  count=0 
  for x in range (len(wage)):
    if (wage[x]<100):
      count=count+1
  print("Number of wages below £100 is ", count)


def menu():
  print()
  print("1 : read from file")
  print("2 : calc wages")
  print("3 : display wages")
  print("4 : get max")
  print("5 : get min")
  print("6 : wages under 100")
  print("7 : exit")

wage=[]
rate=[] 
hours=[] 
name=[] 

for x in range(3):
  login = input("Please enter login : ")
  pwd = input("Please enter password : ")
  if (pwd == "password") and (login=="nataliia"):
    choice =0
    while ( choice!=7 ):
      menu()
      choice=int(input("Choose a menu option : "))
      if ( choice==1): 
        read_hours()
        read_name()
        read_rate()

      elif ( choice==2):
        calc_wages()
      elif ( choice==3): 
        print_wages()
      elif ( choice ==4): 
        get_max()
      elif (choice==5): 
        get_min()
      elif (choice==6): 
        wage100()
      elif (choice==7): 
        print("Goodbye")
      else:
        print("Incorrect choice !") 
    break 
  else: 
    print ("Incorrect login attempt ", x+1)