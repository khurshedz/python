fisrt_number = int(input())
second_nubmer = [int(i) for i in input().split()]
count = 0


if fisrt_number == len(second_nubmer):
    for i in second_nubmer:
        if i % 2 != 0:
            print(i,end=' ')
            count += 1
    print('')
    for i in second_nubmer:
        if i % 2 == 0:
            print(i,end=' ')
            count -= 1
    print('')
    if count >= 1:
        print('NO')
    else:
        print('YES')
