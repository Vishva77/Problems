#find the minimum number of the array
def mininum(array):
    min = array[0]
    for i in range(1,len(array)):
        if (min > array[i]):
            min = array[i]
    return min
print(mininum([7,9,3,2,20]))