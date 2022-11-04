
def DivideElementsByMaximum(array,maximum):
    for i in range(0,len(array)):
        array[i] = array[i] / maximum
    
    return array


def InsertionSort(array_2):
    for i in range(0,len(array_2)):
        
        key = (array_2[i])
        j = i - 1
        while(j >= 0 and key < array_2[j]):

            array_2[j + 1] = array_2[j]
            j = j - 1
          
        array_2[j + 1] = key

    return array_2



def Bucketsort(array):
    Buckets = []
    sortedarray = []
    n = 10
    for i in range(0,10):
        lis = []
        Buckets.append(lis)

    maximum = max(array) + 1
    array = DivideElementsByMaximum(array,maximum)
    
    for j in range(0,len(array)):

        bucketnumber = int(n * array[j])
        array[j] = (array[j] * maximum)
        Buckets[bucketnumber].append(array[j])

    for k in range(0,len(Buckets)):

        arr = InsertionSort(Buckets[k])
        for m in range(0,len(arr)):
            sortedarray.append(arr[m])

    
    
    return sortedarray
    



Array = [4,3,2,1,2.5,3,5,6,2.7,4.4,4.9]
sortedArray = Bucketsort(Array)
print(sortedArray)