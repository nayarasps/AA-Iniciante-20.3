# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

x = list(map(int, input().split()))

for i in range(n-1):
    k = min(abs(x[i+1]-x[i]), abs(x[i-1]-x[i]))
    j = max(abs(x[0]-x[i]), abs(x[-1]-x[i]))

    print(k, j)

print(abs(x[-1]-x[n-2]),abs(x[-1]-x[0]))