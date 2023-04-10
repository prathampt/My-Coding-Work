
import time


def function1():
    print("Hello!")


func2 = function1  # Makes a copy of function and store it in func2...

del function1  # deletes the function1

func2()  # Still func2 works


# _____________-----------------______________--------------_____________------------------____________________

# We can write a function inside a function and also return a function and also give a function as and argument...

# Example_1...

def function2(x):
    if x == 0:
        return print
    elif x == 1:
        return sum


a = function2(1)
print(a)

# Example_2...


def function3(func):
    return func("Hello!")


function3(print)

# Decorator is used to do same things with lots of functions...

# Example...


def decorator1(fun):
    def execute():
        print("Function is executing...")
        time.sleep(3)
        fun()
        time.sleep(3)
        print("Execution is complete.")
    return execute


@decorator1
def myname():
    print("Hello, my name is Pratham...")


myname()

# Or we can also do this... to use the decorator...


def myname1():
    print("Hello, my name is Pratham...")


myname1 = decorator1(myname1)
myname1()
