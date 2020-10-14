# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

a, b = list(map(int,input().split()))
 
if a < b:
    print(0)

elif a == b:
    print("infinity")
else:
    a -= b
    r = 0
    i = 1

    while i ** 2 <= a:
        if a % i != 0: 
            i += 1
            continue

        if i > b: 
            r += 1
        if i == a // i: 
            i += 1
            continue
        if a // i > b:
            r += 1
        i += 1
    
    print(r)
 