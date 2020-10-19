# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())
name = {}

for i in range(n):
    x = input().split()

    if name.get(x[0]) == None:
        name[x[1]] = x[0]

    else:
        name[x[1]] = name.pop(x[0])

print(len(name))
for j in name:
    print(name.get(j), j)
        

    
