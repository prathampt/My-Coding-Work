n = int(input("Enter the number of stages at least 3:\n"))
if n<3:
    exit()
x = input("Any symbol:\n")
print("\n\n\n\n\n" + f"{x} " * n)
for i in range(n-2):
    print(x, " " * (2*n-5), x)
print(f"{x} " * n + "\n\n\n\n\n")