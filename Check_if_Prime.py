# Check if your number is Prime Number or not...
# Made by Pratham Tandale

x = int(input("Enter a Number which you want to check is Prime or not:\n"))


for i in range(2, x):
    remain = x % i
    if remain == 0:
        isprime = False
        break
    else:
        isprime = True
if isprime == False:
    print("Your number", x, "is not a Prime Number...")
else:
    print("Your number", x, "is a Prime Number...\n            :)  :)  :)")
