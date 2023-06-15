
for i in range(1,31):
    for u in range(1,11):
        with open(f"table_of_{i}.txt","a") as table:
            table.write(f" {i} X {u} = {i*u}\n")