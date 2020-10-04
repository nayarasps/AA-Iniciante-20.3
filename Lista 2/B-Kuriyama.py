# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico
from itertools import accumulate

n = int(input())
s = [0] + list(map(int,input().split()))

k = list(accumulate(s))
l = sorted(s)
j = list(accumulate(l))


x = int(input())
for i in range(x):
    p = input().split()
    if p[0] == '1':
        print(k[int(p[2])] - k[int(p[1])-1])

    else:
        print(j[int(p[2])] - j[int(p[1])-1])
        


