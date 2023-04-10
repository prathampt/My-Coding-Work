t = 10
random_list = [35, "Pratham", 1.2, "Hello", 8, 12, 0.9, 79, "Name", 78]
new_dict = {"one": "1", "two": "2", "three": "3"}


def function(var, *args, **kwargs):
    print(f"This is simple variable,{var}")
    print("Following are args...:\n")
    for i in args:
        print(i)
    print("Following are kwargs...:\n")
    for j, k in kwargs.items():
        print(f"Key is {j} and value is {k}")


function(t, *random_list, **new_dict)
random_list.append("Parth")
function(t, *random_list, **new_dict)
