def separate_positive_and_negative_numbers_in_place(array):
  
  p = 0
  n = len(array) - 1

  while p < n:
    if array[p] < 0:
      array[p], array[n] = array[n], array[p]
      n -= 1
    else:
      p += 1

  return array

print(separate_positive_and_negative_numbers_in_place([1, -2, 3, -4, 5]))