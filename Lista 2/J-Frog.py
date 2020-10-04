# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

for i in range(n):
    l = list(map(len, input().split('R')))

    print(max(l) + 1)