# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

vogais = ['a','e','i','o','u']

count = 0

x = input()
for i in range(len(x)):

    if x[i].isdigit():
        if int(x[i]) % 2 != 0:
            count += 1

    else:
        if x[i] in vogais:
            count += 1

print(count)