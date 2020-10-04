# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

l = input().split()

k = []

for i in l[::-1]:
    if i not in k:
        k.append(i)

k.reverse()
print(len(k))
print(' '.join(k))
