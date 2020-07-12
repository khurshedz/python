a = [int(i) for i in input().split()]
solve = []
if len(a) == 4:
    A = a[0]
    B = a[1]
    C = a[2]
    D = a[3]
    for i in range(-100,101):
        if ((A*i**3) + (B*i**2) + (C*i) + D) == 0:
            print(i,end=' ')
