# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

x = 10**9 + 7

a = input()

b = 0
r = 0

for i in a[::-1]:
    if i == 'a':
        r += b
        b = b * 2 % x
    else:
        b += 1
    
r = r % x

print(r)

