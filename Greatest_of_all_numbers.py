a = int(input("Enter your first number:\n"))
b = int(input("Enter your second number:\n"))
c = int(input("Enter your third number:\n"))
d = int(input("Enter your fourth number:\n"))

# if a>b and a>c and a>d:
#     print("Out of your entered numbers, " + str(a) + " is the greatest...")
# elif b>a and b>c and b>d:
#     print("Out of your entered numbers, " + str(b) + " is the greatest...")
# elif c>a and c>b and c>d:
#     print("Out of your entered numbers, " + str(c) + " is the greatest...")
# else:
#     print("Out of your entered numbers, " + str(d) + " is the greatest...")

if a>b:
    f1 = a
else:
    f1 = b

if c>d:
    f2 = c
else:
    f2 = d

if f1>f2:
    print(str(f1) + " is greatest of all numbers...")
else:
    print(str(f2) + " is greatest of all numbers...")

