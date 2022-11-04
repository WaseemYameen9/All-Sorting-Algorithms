    

def sortArrayUsingCountingSort(arr,radix):
    indexes1 = [0 for k in range(10)]
    indexes2 = [0 for k in range(10)] 
    sortedarray = [0 for k in range(len(arr))]
    sum = 0
    
#  This loop creates an array to show how many times a number appear in main array     
    
    for i in range(0,len(arr)):
        num = arr[i]
        num2 = int(num[radix])
        indexes1[num2] = indexes1[num2] + 1

#  This loop adds the elements of indexes1 array 

    for i in range(0,10):
        indexes2[i] = sum + indexes1[i]
        sum = sum + indexes1[i]

#  This loop sorts the array according to the given radix

    for m in range(len(arr)-1,-1,-1):
        element = arr[m]
        elementsPart = int(element[radix])
        indexes2[elementsPart] = indexes2[elementsPart] - 1
        sortedarray = arr[indexes2[elementsPart]]
        # arr = exchangecolumns(arr,indexes2[elementsPart],m)
        
    return sortedarray
        
    
#   Main Radix Sort Function

def RadixSort(arr):
    maximum = max(arr)
    length = len(str(maximum))

# This loop will add zeros and makes all elements length same of the array  
  
    for i in range(0,len(arr)):
       
        num = str(arr[i])
        num = num.zfill(length)
        arr[i] = num


        

    for j in range(length-1,-1,-1):
       arr = sortArrayUsingCountingSort(arr, j)
    return arr
    


l = RadixSort([55,65,444,4567,1])
print(l)