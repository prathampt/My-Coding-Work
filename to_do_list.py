a = "Nothing"
print("Enter your to do task... Press enter when done...")
todo = []
while a != "":
    a = input()
    todo.append(a)
print("Your to-do list is:")
print("--------------------")
for i in todo:
    print(i)
