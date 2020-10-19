# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n, m = list(map(int, input().split()))

x = n // m

kmin = m * x * (x - 1) // 2 + x * (n % m)
kmax = (n - m) * (n - m + 1) // 2

print(str(kmin) + ' ' + str(kmax))