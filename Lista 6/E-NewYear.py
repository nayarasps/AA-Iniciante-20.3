# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())
x = []
y = []

k = 0
g = 0
 
for i in range(n):
    l = list(map(int,input().split()))[1:]
 
    for j in range(len(l)):
        if j > 0 and l[j] > l[j-1]:
            k += 1
            break
        elif j == len(l) - 1:
            g += 1
            y.append(min(l))
            x.append(max(l))
 
count = k * k + 2 * k * g
x.sort()
y.sort()
 
j = 0
for k in x:
    while j < g and y[j] < k:
        j += 1
    count += j
 
print(count)