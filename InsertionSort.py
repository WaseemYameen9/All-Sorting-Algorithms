def InsertionSort(array_2,start,end):
    for i in range(start,end):
        
        key = (array_2[i])
        j = i - 1
        while(j >= start and key < array_2[j]):

            array_2[j + 1] = array_2[j]
            j = j - 1
          
        array_2[j + 1] = key

    return array_2
    

array = [6,5,4,3,1,2]
array = InsertionSort(array, 0, len(array))
print(array)