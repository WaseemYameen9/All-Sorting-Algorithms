

def PigeonHoleSort(arr):
    maximum = max(arr)
    minimum = min(arr)
    Range = maximum - minimum + 1
    
    sortedarraywithZeros = [0 for i in range(Range)]
    sortedarray = []

    # This loop sorts the given array but extra zeros are in the sorted array
    
    for i in range(0,len(arr)):
        idx = arr[i] - minimum
        sortedarraywithZeros[idx] = arr[i]
    
    # This loop first appends the zeros in sorted array that are present in original array
    
    for k in range(0,len(arr)):
        if(arr[k] == 0):
            sortedarray.append(0)

    # This loop now saves the non-zero elements of sorted array in another array
    # so the repition of extra Zeros is removed 
    
    for j in range(0,len(sortedarraywithZeros)):
        if(sortedarraywithZeros[j] != 0):
            sortedarray.append(sortedarraywithZeros[j])
            
    return sortedarray
        



array = [14,5,6,0,0,7,12,3,4,8,10,103,345,69,65,76,89,88]
sortedArray = PigeonHoleSort(array)
print(sortedArray)