# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

p = input()
count = 0
s = ['']

for i in p:
    if s[-1] == i:
        s.pop()
        count += 1
    else:
        s.append(i)


if count % 2 == 0:
    print("No")
else:
    print("Yes")
