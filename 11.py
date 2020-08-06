from functools import reduce
def S(n,k):
    if n >= k: return 2**(k-1)
    return reduce(lambda s, i: s + S(n, k - i - 1), range(n), 0)

print(S(300,300))
