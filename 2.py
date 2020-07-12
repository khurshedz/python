a = int(input())
if a > 0:
  print(sum(range(a+1)))
else:
  print(sum(range(abs(a)+1))*(-1)+1)
