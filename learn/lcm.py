"""def findlcm(n1,n2):
    lcm = n2
    if (n1 > n2):
        lcm = n1
    while(lcm > 0):
        if (lcm % n1 == 0 and lcm % n2 == 0):
            return lcm
        lcm += 1
        
    
print(findlcm(8,7))
"""

def lcmp(n1,n2): #6 , 7
    
    lcm = n2  
    if(n1>n2):
        lcm = n1
    while(True):
        if(lcm % n1 == 0 and lcm % n2 == 0 ): 
            return lcm
        lcm +=1
print(lcmp(6,3))
