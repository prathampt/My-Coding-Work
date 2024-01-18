n = int(input("Enter the number of stages:\n"))

x = input("Any symbol:\n")

for i in range(1, n+1):
    print(" " * (n-i+1), x * (2*i-1), " " * (n-i+1))