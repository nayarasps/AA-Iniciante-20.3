# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

soma = 0

for i in range(n[0]):
    if b[i] == 1:
        soma += a[i]
        a[i] = 0

k = sum(a[0:n[1]])
m = k

for i in range(n[1],n[0]):
    k += a[i]-a[i-n[1]]
    m = max(m,k)

print(soma+m)
