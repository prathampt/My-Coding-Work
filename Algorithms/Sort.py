# Selection Sort...

def Selection_sort(list): # n squared complexity
    for i in range(len(list)):
        s = i
        for j in range(i+1, len(list)):
            if list[s] > list[j]:
                s = j
        list[i],list[s] = list[s],list[i]

    return list

# Bubble Sort...

def Bubble_sort(list): # n squared complexity
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

# Merge Sort...

def Merge_sort(list):
    if len(list) > 1:
        
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        Merge_sort(L)
        Merge_sort(R)

        i = j = k = 0

        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        # If some elements remain...
        while i<len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j<len(R):
            list[k] = R[j]
            j += 1
            k += 1
    
    return list

    
    
l = [11,22,6,27,135,23,36,53,41]
print(Selection_sort(l))
print(Bubble_sort(l))
print(Merge_sort(l))
