


def countingSort(arr):
    maximum = max(arr)
    indexes = [0 for k in range(maximum+1)]
    sortedarray = []
    for i in range(0,len(arr)):
        indexes[arr[i]] =indexes[arr[i]] + 1
    
    for i in range(0,maximum+1):
        num = indexes[i]
        if(num == 0):
            continue
        numberofAppearence = int(indexes[i])
        for m in range(0,numberofAppearence):
            sortedarray.append(i)
            
    return sortedarray
    
    



array = [0,2,1,9,9,4,5,6]

sortedArray = countingSort(array)
print(sortedArray)

