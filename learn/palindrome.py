'''def palindrome(string):
    i = 0
    j = len(string) - 1
    while(i < j):
        if(string[i] != string[j]):
           return print("not a palindrome")
        i += 1
        j -= 1
    return print("palindrome")


palindrome("3478843")'''

def string(n):
    f = 0
    l = len(n)-1
    while(f <= l):
        if (n[f] != n[l]):
            return ("not palindrome")
        else :
            f += 1
            l -= 1
    return ("palindrome")
print(string("malayalam"))