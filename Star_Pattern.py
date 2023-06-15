
n = int(input("Enter an Integer...\n"))
m = input("Enter just 't' or 'f'...\n")
o = input("Enter any symbol...\n")
print('\n\n')
if m == 't' or m == 'T':
    for i in range(1, n+1):
        print(o * i)
elif m == 'f' or m == 'F':
    for i in range(1, n+1):
        print(o * (n-i+1))
