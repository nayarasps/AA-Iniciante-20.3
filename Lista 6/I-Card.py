# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

mod = 10**9 + 7

def bet(l, k):
    saida = 0
    l.sort()
    resultado = 1

    for i, j in enumerate(l):
        if (i + 1 < k):
            continue
        if (i - k >= 0):
            resultado *= i
            resultado /= i - k + 1
        
        saida += (j * resultado) % mod

    return saida

n = int(raw_input()) 

for i in range(1, n+1):
  n, k = list(map(int, raw_input().split()))
  l  = list(map(int, raw_input().split()))
  print ('Case #%d: %d' % (i, bet(l, k)))
