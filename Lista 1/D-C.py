# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

t = int(input())


for i in range(t):
    count = 0

    x = list(map(int, input().split()))

    stop = x[2]

    v1 = x[0]
    v2 = x[1]
    while v1 <= stop or v2 <= stop:
        if v1 <= v2:
            v1 += v2
        else:
            v2 += v1

        count += 1

    print(count - 1)