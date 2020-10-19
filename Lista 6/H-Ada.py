# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

mod = 10**9 + 7
m = 10**6 + 1

l1 = [1]*m
l2 = [1]*m

def getMod(x):
    return ((x%mod) + mod)%mod

def fact(x,y):
  if (x < y):
    return 0
  return getMod(getMod(l1[x]*l2[y])*l2[x-y])

for i in range(1,m):
    l1[i] = getMod(l1[i-1]*i)
    l2[i] = pow(l1[i], mod-2, mod)

while True:
    try:
        n, a ,b, d = map(int,input().split())

        k = fact(n, a)
        j = fact(b, d)

        print(getMod(k*pow(j,a,mod)))

    except EOFError:
        break

