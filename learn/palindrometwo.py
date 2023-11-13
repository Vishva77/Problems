def palindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        rem = n % 10
        rev = (rev * 10) + rem
        n //= 10
    if (rev == temp):
        print("palindrome")
    else:
        print("not palindrome")
palindrome(343)