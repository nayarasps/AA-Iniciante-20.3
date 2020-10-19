# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

t = int(input())

for i in range(t):
    n, k = list(map(int,input().split()))
    l = ['a'] * n
    
    for j in range(n-2,-1,-1):
        if (k <= n-j-1):
            l[j] = 'b'
            l[n-k] = 'b'
            print(''.join(l))
            break
        k -= n-j-1
    