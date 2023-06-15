
for i in range(1,11):
    for u in range(1,11):
        with open(f"table{i}.txt","a") as table:
            table.write(f" {i} X {u} = {i*u}\n")