def lcm(n1,n2):
    lcm = n2
    small = n2
    if (n1<n2):
        lcm = n1
    else:
        small=n1
    g = lcm
    while(lcm%small!=0):
        lcm=lcm+g
    return lcm
print(lcm(12,6))