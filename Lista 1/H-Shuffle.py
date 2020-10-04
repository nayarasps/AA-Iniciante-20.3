# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

import collections

n = int(input())

for i in range(n):
    a = input()
    b = input()
    k = len(b) - len(a)
    bol = False

    count = len(a)

    if len(b) < len(a):
        bol = True
        print('NO')
    elif len(b) == len(a):
        if collections.Counter(b) == collections.Counter(a):
            bol = True
            print('YES')
    else:
        for i in range(k+1):
            t = b[i:count]
            if collections.Counter(t) == collections.Counter(a):
                print('YES')
                bol = True
                break
            else:
                count += 1
    if bol == False:
        print('NO')