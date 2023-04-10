print("Welcome to Celsius-Fahrenhit Convertor...")
way = input("Please type 'cf' to convert Celsius into Fahrenhit,\nor type 'fc' to convert Fahrenhit into Celsius...\n")
value = int(input("Please Enter value:\n"))

def convertor(value):
    if way == "cf":
        return ((value*9)/5)+32
    elif way == "fc":
        return ((value-32)*5)/9
    else:
        exit()

print(convertor(value))