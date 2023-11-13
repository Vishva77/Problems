def bubble_sort(arr):
    l = len(arr)-1
    for i in range(l):
        for j in range(l-i):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j+1] = arr[j+1] ,arr[j]
    return arr
print(bubble_sort([1,5,21,4,2,7,6,9,10,11,3,14,2,17,19,20,8,25,28,29,37]))