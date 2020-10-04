# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

l = list(map(int, input().split()))
l.sort()

j = 0
count = 0

for i in range(n):
    while abs(l[j] - l[i]) >= 5:
        j += 1
    count = max(count, i-j)
        

print(count+1)

