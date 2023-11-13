def sum_of_digits(n):
    odd = 0
    even = 0
    while(n > 0):
        rem = n % 10
        if(rem % 2 == 0):
            even += rem  # Use += to accumulate even digits
        else:
            odd += rem  # Use += to accumulate odd digits
        n //= 10
    diff = abs(odd - even)  # Calculate the absolute difference between odd and even sums
    print(diff)

sum_of_digits(3276476)
