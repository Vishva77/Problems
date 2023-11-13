# find the maximum number
def maxnum(array):
    max = array[0]
    for i in range(1,len(array)):
        if (max < array[i]):
             max = array[i]
    return max
print(maxnum([1,3,6,90,4]))