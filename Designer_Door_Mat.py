n,m = map(int, input().split())
string = "WELCOME"
for i in range(n//2):
    for j in range(m//2 - 1 - 3*i):
        print("-", end="")
    for k in range(2*(i+1) - 1):
        print(".|.", end="")    
    for j in range(m//2 - 1 - 3*i):
        print("-", end="")
    print()
        
print(string.center(m,"-"))


for i in range(n//2,0,-1):
    for j in range(m//2 - 1 - 3*(i-1)):
        print("-", end="")
    for k in range(2*i - 1):
        print(".|.", end="")    
    for j in range(m//2 - 1 - 3*(i-1)):
        print("-", end="")
    print()


    
