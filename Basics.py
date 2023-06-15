# a = 10
# b = "Hello"
# c = 0

# print(a+c)
# print(a**c)
# z = input()
# print(z)

# if a == 100:
#     print(a)
#     print("This")
# elif c == 10:
#     print(c)
# elif c != 3:
#     print(3)
# else:
#     print(b)

# a,c = c,a
# print(a)

# t = a
# a = c
# c = t


# a = 98
# b = 78
# c = 78

# print(max(a,b,c))

# if a>b and a>c:
#     print(a)
# elif b>c and b>a:
#     print(b)
# else:
#     print(c)

# def fun(n):
#     product = 1
#     for i in range(1,n+1):
#         product *= i
#     return product

# print(fun(7))

# def fun1(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fun1(n-1)

# print(fun1(7))

# list1 = [1,2,3,4,5,23,475,3849,72,17,27,382]

# # print(list1[4:1:-1])
# # sum = 1
# # for i in range(1,4):
# #     sum = sum * list1[i]
# # print(sum)
# # n = 7
# # for i in range(n):
# #     a = int(input())
# #     list1.append(a)

# print(list1)
# list1.remove(382)
# print(list1)
# list1.insert(5, 47)
# print(list1)

# for i in list1:
#     print(i)

# i = 0
# while i <10:
#     print("Hello")
#     i +=1

# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(17))

# f = open("poem.txt","a")
# f.write("Hello this is what I am writing for sujal...")
# f.write("hello")
# # x = f.read()
# f.close()

# for i,j in enumerate(list1):
#     print(i,j)


# def bubble_sort(list):
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] < list[j]:
#                 list[i],list[j] = list[j],list[i]
#     return list

# list1 = [1,22,3,44,5,23,475,3849,72,17,27,382]
# print(list1)
# print(bubble_sort(list1))
# list1 = list1[::-1]
# print(list1)

# n = 5
# for i in range(n):
#     for j in range(i+1,n):
#         print(" ",end="")
#     for k in range(n-i-1,n):
#         print(i+1,end="")
#     print()

# names1 = ["Mango", "Banana", "Cherry"]
# names2 = names1
# names3 = names1[:]
# names2[0] = "Orange"
# names3[1] = "Grapes"
# sum = 0
# for ls in (names1, names2, names3):
#     print(ls)
#     if ls[0] == "Orange":
#         sum += 1
#     if ls[1] == "Grapes":
#         sum += 10
# print(sum)

# print(18==18.0)
# print('18'==18.0)
# print(18 is 18.0)
# print('18' is 18.0)
# print(int(2.99))
# print(ord('a'))
# print(ord('A'))
# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()

# for i in range(0,1):
#     print(i)

# def b_search(lst,x,low,high):
#     if high >= low:
#         mid = (high+low)//2
#     # If found at mid, then return it
#         if lst[mid] == x:
#             return mid
#  # Search the left half
#         elif lst[mid] > x:
#             return b_search(lst, x, low, mid-1)
#  # Search the right half
#         else:
#             return b_search(lst, x, mid + 1, high)
#     else:
#         return -1
# lst = [3, 4, 5, 6, 7, 8, 9]
# high = len(lst)-1
# low = 0
# val = int(input())
# x = b_search(lst,val,low,high)
# if x == -1:
#  print("Element not found")
# else:
#  print("Element found")

# str1 = 'abc'
# str2 = 'abcda'
# print(str1[0] is str2[4])

# def gcd(x,y):
#     global p 
#     p = 10
#     if y>x:
#         return gcd(y,x)
#     elif x%y == 0:
#         return y
#     else:
#         return gcd(y,x%y)

# print(gcd(20, 30))
# print(p)

# def rand(x):
#     a = 10
#     b = 3
#     m = 7
#     return (a*x + b) % m

# for i in range(10):
#     print(rand(i))

# print(ord("a"))
# print(chr(97))


