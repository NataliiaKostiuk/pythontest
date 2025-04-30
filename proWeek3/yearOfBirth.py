from handler import getName, getAge


def getYearOfBirth():
    name = getName()
    print(f"Hello {name}")
    age = getAge()
    print(f"You was birn in {2025-age} year")

getYearOfBirth()    