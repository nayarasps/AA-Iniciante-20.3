# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

for i in range(n):
    s = list(filter(None,input().split('0')))

    s.sort(key=len, reverse=True)

    if len(s) == 0:
        print('0')
        continue

    r = ''

    for j in s[::2]:
        r += j

    print(len(r))



    