def primenum(n):
    p=n//2
    for i in range(2,p+1):
        if (n%i==0):
            return "it is not a prime"

    return "it is prime"

print(primenum(22))