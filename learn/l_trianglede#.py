# Write a program to print like a left-angled triangle af #

def pattern(n):
    for r in range(1,n+1): #5 -->
        for c in range(1,n+1):#1
            if (c <= n-r ):#1 <= 4 , 2 <= 4, 3<=4, 4<=4, 5<=4
                print(" ",end="")
            else:
                print("#",end="")
        print()

print(pattern(6))