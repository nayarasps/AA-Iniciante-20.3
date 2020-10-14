# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

x = 10**9 + 7

n,m = list(map(int, input().split()))

l = []

for i in range(n):
    l.append(input())

r = []

for j in range(m):
    s = set()
    for k in range(n):
        s.add(l[k][j])
    r.append(len(s))

count = 1
for y in r:
    count = (count * y) % x

print(count)
    