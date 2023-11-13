def divid(n):
    count = 0
    temp = n
    while(n > 0):
        sd = n % 10
        if (sd != 0 and temp % sd == 0):
            count += 1
        n = n // 10
    return count
print(divid(137040))