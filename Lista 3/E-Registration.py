# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())
count = 0
senhas = {}

for i in range(n):
    p = input()

    if p not in senhas:
        print("OK")
        senhas[p] = 0
    else:
        if senhas[p] == 0:
            senhas[p] = 1
            print(p + str(senhas[p]))
        else:
            senhas[p] += 1
            print(p + str(senhas[p]))
            
    