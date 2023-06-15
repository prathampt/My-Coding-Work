
from math import sqrt

# x = int(input("Enter a Number who's Operation you want to do:\n")) 

class Calculator:

    def __init__(self, no):
        self.no = no
    
    def square(self):
        print(f"The square of {self.no} is {self.no * self.no}")                       # or write **2 for square

    def cube(self):
        print(f"The cube of {self.no} is {self.no * self.no * self.no}")             # or write **3 for cube

    def root(self):
        n = self.no
        r = sqrt(n)
        print(f"The root of {self.no} is {r}")                                      # or write **0.5 for squareRoot
    
    @staticmethod
    def greet():
        print("Hello!")

# num1 = Calculator(x)
# num1.greet()
# num1.cube()
# num1.root()
# num1.square()
