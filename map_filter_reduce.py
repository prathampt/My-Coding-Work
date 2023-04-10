#-------------------Map---------------------------
given_list = ['0','1','2','3','4','5','6','7','8','9'] # Shortest Code for this Work...
func_list = [lambda x:x**2, lambda x:x**3, lambda x:x**4, lambda x:x**5]
int_list = list(map(int, given_list))
for i in range(len(int_list)):
    output_list = list(map(lambda x:x(int_list[i]), func_list))
    print(output_list)
#-----------------------Filter-----------------------
given_list = ['0','1','2','3','4','5','6','7','8','9']
int_list = list(map(int, given_list))
def num_greater(num):
    return num > 5   # This will return True if the num is greater than 5
int_list_2 = list(filter(num_greater, int_list)) # If the function returns True then the filter will include it into list...
print(int_list_2)
#----------------------Reduce---------------------------
from functools import reduce
given_list = ['0','1','2','3','4','5','6','7','8','9']
int_list = list(map(int, given_list))
sum = reduce(lambda x,y:x+y, int_list) # Reduces the function and performs it on all list items...
print(sum)