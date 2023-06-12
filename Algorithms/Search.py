# Linear Search...

def linear_search(list, element):
    for index, i in enumerate(list):
        if i == element:
            return index
    return False

# Binary Search...

def binary_search(list, element, p2, p1=0):
    mid = (p1+p2)//2
    if list[mid] == element:
        return True
    elif list[mid] < element:
        p1 = mid+1
    elif list[mid] > element:
        p2 = mid-1
    else:
        return False
        
    return binary_search(list, element,p1,p2)


l = [1,2,6,7,15,23,36,53,411]
print(linear_search(l, 7))
print(binary_search(l, 7,9))