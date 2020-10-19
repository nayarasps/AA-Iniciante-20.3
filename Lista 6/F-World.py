# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

from math import factorial

n, m, t = list(map(int,input().split()))

count = 0
for i in range(4, min(t-1, n)+1):
    x = factorial(n) // factorial(n-i) // factorial(i)
    
    for j in range(1, min(t-4, m)+1):
        if i + j == t:
            count += x * factorial(m) // factorial(m-j) // factorial(j)

print(count)