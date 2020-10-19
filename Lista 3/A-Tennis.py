# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico


n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

count = 0
j = x[0]

for i in range(1,n):

    if count >= k:
        break
    
    if j > x[i]:
        count += 1

    else:
        j = x[i]
        count = 1

print(j)


