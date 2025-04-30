from handler import getName, getAge
def getData():
    name = getName()
    age = getAge()
    city = input("Enter your city: ")
    data = (name, age, city)
    return data


result = getData()
print(result)
name, age , town = result
print(town)