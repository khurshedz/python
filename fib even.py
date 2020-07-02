def f(n):
    a, b, c = 0, 1, []
    while 1:
        if a % 2 == 0:
            c.append(a)
            if len(c) == n:
                for i in c:
                    print(i,end=' ')
                break
        a, b = b, a+b
    print()
f(4)
