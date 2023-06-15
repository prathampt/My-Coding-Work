# Calculator...
import sys


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def square(num1):
    return num1**2


def cube(num1):
    return num1**3


def squareroot(num1):
    return num1**0.5

if __name__=='__main__':

    b = False
    print("\nWel-come to our calculator...")
    b = bool(input("Do you want to use the calculator? Type '1' if yes and leave blank i.e. just press Enter if don't...\n"))
    if b == False:
        sys.exit()

    while b:
        num1 = int(input("Enter first number...\n"))
        oper = input("Enter operation...\n + for Addition\n - for Subtraction\n * for Multiplication \n / for Division \n sq for Square \n cube for Cube \n sqrt for Square Root \n")
        if oper == "+" or oper == "-" or oper == "*" or oper == "/":
            num2 = int(input("Enter second number...\n"))
        if b == False:
            break
        elif oper == "+":
            print(f"{num1} {oper} {num2} = {addition(num1, num2)}")
        elif oper == "-":
            print(f"{num1} {oper} {num2} = {subtraction(num1, num2)}")
        elif oper == "*":
            print(f"{num1} {oper} {num2} = {multiplication(num1, num2)}")
        elif oper == "/":
            print(f"{num1} {oper} {num2} = {division(num1, num2)}")
        elif oper == "sq":
            print(f"{num1}'s square is equal to {square(num1)}")
        elif oper == "cube":
            print(f"{num1}'s cube is equal to {cube(num1)}")
        elif oper == "sqrt":
            print(f"{num1}'s square root is equal to {squareroot(num1)}")
        else:
            print("That function is currently unavailable. Please contact the Programer...")
        b = bool(input("Do you want to use the calculator again? Type '1' if yes and leave blank i.e. just press Enter if don't...\n"))
