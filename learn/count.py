def length(x):
    count = 0
    while(x>0):
        count += 1
        x //=10
    return count

print(length(1))
