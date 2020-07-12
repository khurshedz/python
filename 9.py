first_n = int(input())
scnd=[int(i) for i in input().split()]
sum_scnd = 0
mult_scnd = 1
if first_n == len(scnd):
    for i in scnd:
        if i > 0:
            sum_scnd += i
    max_scnd_index = scnd.index(max(scnd))
    min_scnd_index = scnd.index(min(scnd))
    max_scnd = max(scnd)
    switcher = len(scnd)//2
    if max_scnd in scnd[:switcher]:
        c = scnd[max_scnd_index+1:min_scnd_index]
    else:
        c = scnd[min_scnd_index+1:max_scnd_index]
    for i in c:
        mult_scnd *= int(i)
    print(sum_scnd, mult_scnd)
