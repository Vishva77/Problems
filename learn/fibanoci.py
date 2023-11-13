#fibanosi series
def fibanoci(n):
    x = 0
    y = 1
    if (n == 0):
        print ("NO VALUE")
    elif (n == 1):
        print(x,end =" ")
    elif (n == 2):
        print(x,end =" ")
        print(y,end =" ")
    else :
        print(x,end =" ")
        print(y,end =" ")
        count = n-2
        while(count > 0):
            z = x + y
            print(z,end=" ")
            x = y
            y = z
            count -=1
(fibanoci(10))
