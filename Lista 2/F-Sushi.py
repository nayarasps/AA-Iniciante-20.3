# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

x = list(map(int, input().split()))
antes = 0
count = 0
l = []

for i in x:
    if i != antes:
        l.append(count)
        count = 1
        antes = i
    else:
        count += 1

l.append(count)
k = 0

for i in range(1,len(l)-1):
    n = min(l[i], l[i+1])
    if n > k:
        k = n

print(k*2)

    
