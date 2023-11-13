def sqr(n,d):
    s = n//2 #8
    while s:
        if s * s < n and ((s+1)*(s+1)) > n: #81 < 19 and 100  > 19
           break
        elif s * s > n:  #81 > n
            s = s//2    #9//2 = 4
        else:
            s = s+1 
    dp = 0.1
    r = 1
    while d:
        s = round(s+dp,r)
        while s*s < n:
            s = round(s+dp,r)
        s = round(s-dp,r)
        dp = dp/10
        d = d-1
        r += 1
    return s


print(sqr(16,0))
