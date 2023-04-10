
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


        
list = []
student1 = Student("Pratham", 612203176, 10)
student2 = Student("Parth", 612205076, 8)
student3 = Student("Rohit", 612203006, 9)
temp = [student1,student2,student3]


temp[0].mark_attendance()