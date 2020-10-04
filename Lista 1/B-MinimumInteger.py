# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

q = int(input())

for i in range(q):
    x = list(map(int,input().split()))
    
    if x[2] < x[0]:
        print(x[2])
    
    else:
       y = (x[1] // x[2]) + 1
       print(y*x[2])