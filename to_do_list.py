a = "Nothing"
print("Enter your to do task... Press enter when done...")
todo = ["Code", "Write"]
while a != "":
    a = input()
    todo.append(a)
print("Your to-do list is:")
print("--------------------")
for i in todo:
    print(i)
