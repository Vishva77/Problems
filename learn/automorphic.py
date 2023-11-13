# a number is called an automorphic number if and only if the square of the given number ends with the same number itself. For example, 25, 76 are automorphic ...


def number(n):
   x = n**n  #given = 25  =>625
   while(n>0): #25>0
       if (n%10  != x%10):  #5 !=5
          return print("not automorphic number")
       n=n//10  # 2
       x=x//10  # 62
   print("automorphic number")
number(6)