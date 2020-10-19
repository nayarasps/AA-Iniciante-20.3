# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n, k = list(map(int, input().split()))

m = list(map(int, input().split()))

s = set()
tela = []

for i in m:
    if len(tela) < k:
        if i not in s:
            tela.append(i)
            s.add(i)
    else:
        if i not in s:
            s.remove(tela.pop(0))
            tela.append(i)
            s.add(i)

tela.reverse()
print(len(tela))

r = ''
for i in tela:
    r += str(i) + ' '

print(r.rstrip())







