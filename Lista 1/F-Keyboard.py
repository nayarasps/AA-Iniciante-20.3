# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

t = int(input())

for j in range(t):
    x = list(input())
    count = 1

    while count < len(x):
        if len(x) == 1:
            s = x
            break

        if x[count] == x[count-1]:
            x[count] = ''
            x[count-1] = ''
            count += 2
        else:
            count += 1
            
    x = sorted(list(set(x)))
    print(''.join(x))

