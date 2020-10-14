# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

x = 10**9 + 7

n = int(input())

a = 27 ** (n % x)
b = 7 ** (n % x)

r = (a-b) % x

print(r)