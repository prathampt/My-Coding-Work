
class Programmer:
    company = "Google"

    def salaryOf(self):
        print(f"The salary of {self.name} is {self.salary}")


Parth = Programmer()
Pratham = Programmer()
Parth.salary = 100000
Pratham.salary = 200000
Parth.name = "Parth"
Pratham.name = "Pratham"
Parth.salaryOf()
Pratham.salaryOf()

# Same above programme using constructor...


class Programmer2:
    company = "Microsoft"

    def __init__(self):
        print(f"New Programmer2 is created...")

    def data(self):
        print(self.name, self.salary, self.phoneNo)


ppt = Programmer2()
ppt.mm = 'hello'
ppt.name = "Pratham"
ppt.salary = 1000000
ppt.phoneNo = 9766504701
ppt.data()

# Insted of above we can write...


class Programmer3:
    company = "Google"

    def __init__(self, name, salary, phoneNo):
        self.name = name
        self.salary = salary
        self.phoneNo = phoneNo
        print(f"New programmer is created... with name {self.name}")

    def Data(self):
        print(self.name, self.salary, self.phoneNo)


pra = Programmer3("Pratham", 1000000, 9766504701)
pra.Data()


class Employee(Programmer3):

    def __init__(self, name, salary, phoneNo, post):
        self.post = post
        self.name = name
        self.salary = salary
        self.phoneNo = phoneNo

    def Post(self):
        print(f"Post of {self.name} is {self.post}")

prad = Employee("Prad", 100000, 8389298738, "Head")
print(prad.company)
prad.Data()
prad.Post()
