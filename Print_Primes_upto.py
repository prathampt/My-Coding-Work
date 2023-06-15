# Print Prime Numbers upto you want...
# Made by Pratham Tandale

x = int(input("Enter the number upto which you want Prime Numbers:\n"))
prime_numbers = [2]
for a in range(2, x+1):
    prime = False
    for i in range(2, a):
        remain = a%i
        if remain == 0:
            prime = False
            break
        else:
            prime = True
    if prime == True:
        prime_numbers.append(a)

print("\n\nHere is your list of Prime Numbers upto", x, ":\n", prime_numbers)
print(f"Total number of Primes are : {len(prime_numbers)}")