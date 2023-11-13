def length(v):
    temp = v
    count = 0
    value = v
    arm = 0
    while(v>0):
        count += 1
        v //= 10

    
    while(value > 0):
        rem = value %10
        arm = (rem ** count)+ arm
        value = value // 10

    
    if(temp == arm):
            return print("armstrong")
    else:
            return print("mot armstrong")
length(153)

    