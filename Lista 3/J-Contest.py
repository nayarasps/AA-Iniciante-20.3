# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n, m = list(map(int, input().split()))
c = list(map(int, input().split()))

r = ['0'] * m
x = [0] * (n + 1)
y = [0] * (m + 1)
count = 1

for i in range(m):
    x[c[i]] += 1
    y[x[c[i]]] += 1
    
    if y[count] == n:
        r[i] = '1'
        count += 1

print(''.join(r))