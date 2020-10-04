# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

for i in range(n):
    x = input().split()

    r = int(x[0]) * int(x[1])
    k = int(x[0])-1

    if r % k == 0:
        m = (r // k) - 1
        print(m)
    else:
        m = r // k
        print(m)
        

