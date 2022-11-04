def minimum(array , start):
    minimumNumber = array[start]
    minimumIndex = start
    for i in range(start , len(array)):
        if(minimumNumber > array[i]):
            minimumNumber = array[i]
            minimumIndex = i
    return minimumIndex    



def SelectionSort(array , start , end):
    for i in range (start,end):
        minIndex = minimum(array, i)
        temp = array[i]
        array[i] = array[minIndex]
        array[minIndex] = temp

    return array


array = [1,5,3,6,8,2,0]
array = SelectionSort(array, 0, len(array))
print(array)