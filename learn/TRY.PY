#how to search element in sorted infinite array

#INPUT : Array = [1,2,3,4,5,7,8,9,10,11,12,14,17,19,20,25,28,29,37,...]  Target = 17
#OUTPUT : 12

def binary_search_infinite(arr, target):
    left = 0 
    right = 1 

    while arr[right] < target:
        left = right
        right *= 2

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
            right = mid - 1  

    return -1  

print(binary_search_infinite([1,2,3,4,5,7,8,9,10,11,12,14,17,19,20,25,28,29,37], 17))