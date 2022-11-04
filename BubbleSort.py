def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(end,start,-1):
            if(array[j] < array[j - 1]):
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return (array)

array = [4,5,2,7,8,2,1,0,0,2]
array = BubbleSort(array, 0, len(array)-1)
print(array)