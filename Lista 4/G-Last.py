# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

from math import pow

n = int(input())
r = 0

for i in range(n):
    a,b = list(map(int, input().split())) 

    if a == 0 and b > 0:
        print(0)
        continue
    if a > 0 and b == 0:
        print(1)
        continue
    
    a = int(a%10)
    b = int(b%4)

    if b == 0:
        b = 4
    

    print((a**b) % 10)


