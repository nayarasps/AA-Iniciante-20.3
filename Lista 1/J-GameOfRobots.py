# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

nk = input().split()
id = input().split()

n = int(nk[0])
k = int(nk[1])

for i in range(n):
    if (i >= k):
        break
    k -= i
print(id[k-1])