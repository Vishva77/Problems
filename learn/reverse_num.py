def count(n):
    count = 0
    while(n>0):
        count +=1
        n //=10
    return count #3
def swap(n):  #567
  ld = n % 10   #ld = 7
  length = count(n) - 1  #length = 2
  power = 10 ** length #power = 100
  fd = n // power #fd = 5
  n = n%power #n = 67
  n = n//10 # n = 6 
  n =(n*10) + fd # n = 65
  ld = ld * power #ld = 700
  n = ld + n  # 700 +65
  print(n)
swap(567)