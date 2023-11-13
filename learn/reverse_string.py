def reverse_string(n):
    start = 0
    end = len(n)-1
    n = list(n)
    while(start < end):
        temp = n[start]
        n[start] = n[end]
        n[end] = temp
            
        start += 1
        end -= 1
    return ("".join(n))

print(reverse_string("vishva"))

