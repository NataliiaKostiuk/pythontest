name = "Natalii Kostiuk"
print(name.lower())
print(name.upper())
print(name.capitalize())
print(len(name))
print( name.find(" "))
print(name.strip())
pos = name.find(" ")
shotName=name[0]+name[pos+1:len(name)]
print(shotName)