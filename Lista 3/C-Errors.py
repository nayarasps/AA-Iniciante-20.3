# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

soma1 = sum(c1)
soma2 = sum(c2)
soma3 = sum(c3)

print(soma1 - soma2)
print(soma2 - soma3)