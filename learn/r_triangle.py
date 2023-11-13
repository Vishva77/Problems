def rtriangle(n):
    l = len(n)
    for r in range(1,l+1):
        for c in range(0,r):
             print(n[c],end="")
        print()

rtriangle("VISHVA")