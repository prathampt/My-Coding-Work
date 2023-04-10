def fibonacci_loop(n):
    a = 0
    b = 1
    for i in range(n-1):
        a = a + b
        a,b = b,a
    return b


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
# If we run the programe from here then only __name__ will be equal to __main__...
# Thus it should be used to write programs which we want to import...
if __name__=='__main__':
    fibonacci_list = []
    n = int(input("Enter any number...\n"))
    for i in range(0,n+1):
        a = fibonacci_loop(i)
        fibonacci_list.append(a)

    print(fibonacci_list)
