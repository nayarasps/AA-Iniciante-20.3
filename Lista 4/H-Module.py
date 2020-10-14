# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n,m = list(map(int, input().split()))

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()

l = []

for i in range(n):
    l.append((l2[0]-l1[i]) % m)

l = list(set(l))
l.sort()

for j in l:
    r = []

    for k in range(n):
        r.append((l1[k]+j)%m)
    
    r.sort()

    if r == l2:
        print(j)
        break