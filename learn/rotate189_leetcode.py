#Given an integer array nums,
#rotate the array to the right by k steps, where k is non-negative.


def rotate(nums, k):
    k = k % len(nums)  
    rotated_nums = [0] * len(nums) 
    
    for i in range(len(nums)):
        rotated_nums[(i + k) % len(nums)] = nums[i] 
        
    for i in range(len(nums)):
        nums[i] = rotated_nums[i] 
    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7],3)) 


# def rotate(nums, k):
#     k = k % len(nums)  
    
#     def reverse(arr, start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1

#     reverse(nums, 0, len(nums) - 1)  # Reverse the entire array
#     reverse(nums, 0, k - 1)  # Reverse the first part
#     reverse(nums, k, len(nums) - 1)  # Reverse the second part
#     return nums
    
# print(rotate([1, 2, 3, 4, 5, 6, 7],3))