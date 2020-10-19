# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

for i in range(n):
    v = int(input())
    l = list(map(int, input().split()))

    s = ''
    da = {}

    e = v
    d = 0
    for j in range(v):
        da[l[j]] = j

    for t in range(1,v+1):
        e = min(e,da[t])
        d = max(d,da[t])
        if (d-e)+1 > t:
            s += '0'
        else:
            s += '1'
    print(s)

    