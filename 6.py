a=list(input())
s='ABCDEFGH'
b='12345678'

if len(a)==5 and int(a[1]) in range(1,9) and int(a[4]) in range(1,9) and a[0] in s and a[3] in s and a[2]=='-':
    x1=b.find(a[1])+1
    x2=b.find(a[4])+1
    y1=s.find(a[0])+1
    y2=s.find(a[3])+1
    if abs(x2-x1)==2 and abs(y2-y1)==1 or abs(x2-x1)==1 and abs(y2-y1)==2:
        print("YES")
    else:
        print("NO")
else:
    print('ERROR')
