# # Procedure Programing...
# # Student 1

# name1 = "Pratham"
# mis1 = 612203176
# div1 = 10
# university_name = "COEP"
# print(name1,mis1,div1,university_name)

# # Student 2

# name2 = "Parth"
# mis2 = 612205076
# div2 = 8


# university_name = "COEP"


# # Student 3

# name3 = "Rohit"
# mis3 = 612203006
# div3 = 9
# university_name = "COEP"



















# # Object Oriented Programing...

# class Student:

#     university_name = "COEP"
    
#     def __init__(self, name, mis, div):
#         self.name = name
#         self.mis = mis
#         self.div = div

#     def print_data(self):
#         print(self.name, self.mis, self.div, self.university_name)
        

# student1 = Student("Pratham", 612203176, 10)
# student2 = Student("Parth", 612205076, 8)
# student3 = Student("Rohit", 612203006, 9)

# student1.print_data()

# student2.print_data()
# student2.university_name = "Pict"
# student2.mis = 612203176
# student2.print_data()
# student3.print_data()
# Student.university_name = "IIT"
# student2.print_data()
# student3.print_data()























# Object Oriented Programing...

class Student:

    university_name = "COEP"    
    attendance = 0

    def __init__(self, name, mis, div):
        self.name = name
        self.mis = mis
        self.div = div

    def print_data(self):
        print(self.name, self.mis, self.div, self.university_name)

    def mark_attendance(self):
        # self.attendance = 0
        self.attendance += 1
        print("Now current attendance is", self.attendance)

    @staticmethod
    def greet():
        print("Hello!")


        

student1 = Student("Pratham", 612203176, 10)
student2 = Student("Parth", 612205076, 8)
student3 = Student("Rohit", 612203006, 9)

student1.print_data()
# Changing object attribute...
print(student1.attendance)
student1.mark_attendance()
print(student2.attendance)


# Changing Class attribute...
Student.attendance = 10
print(Student.attendance)
print(student1.attendance)
print(student3.attendance)


student1.greet()

