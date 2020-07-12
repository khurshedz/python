digits = [int(i) for i in input().split()]
fst_n = digits[0]
scd_n = digits[1]
thd_n = digits[2]

solution = fst_n * scd_n

if solution == thd_n:
    print('YES')
else:
    print('NO')
