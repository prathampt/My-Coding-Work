
# Health Management System...
# The shortest code in all the comments...

def Health_Management(user):
    '''No need to make any file or folder...'''
    def date_time():
        import datetime
        return datetime.datetime.now()
    print(f"Hello, {user}.")
    x = int(input("\nEnter '1' if you want to record data or Enter '2' to see the data...\n"))
    y = int(input("\nWhose data you want to see? Enter the digits according to following...\n\t1:Pratham\n\t2:Parth\n\t3:Pravin\n"))
    z = int(input("Choose from Exercise or Diet... Enter '1' for Exercise or '2' for Diet...\n"))

    if x == 1:
        a = input("Enter the Information...\n")
        with open(f"{z}_{y}.txt", "a") as f:
            f.write(f"[{date_time()}] {a}")
            print("Data added successfully...\nYou can check the data by running the function again...")
    elif x == 2:
        try:
            with open(f"{z}_{y}.txt") as f:
                info = f.read()
                print(info)
        except Exception as e:
            print("You must have to Enter the Data befor you read it...\nTry Entering the data...")

Health_Management("Pratham")
Health_Management("Pradnyesh")
