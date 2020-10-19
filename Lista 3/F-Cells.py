# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n, m = list(map(int, input().split()))

r = ''
colunas = set()
linhas = set()
total = n ** 2

for i in range(m):
    l,c = list(map(int,input().split()))
    linhas.add(l)
    colunas.add(c)

    count = len(linhas) * n + len(colunas) * n - (len(linhas) * len(colunas))
    r += str(total - count) + ' '

print(r.rstrip())



    

