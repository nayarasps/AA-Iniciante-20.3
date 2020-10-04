# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

book = input().split()
order = input().split()

p =[0] * n
count = -1
s = ''

for i in range(n):
    p[int(book[i])-1] = i


for i in range(n):
    if (count < p[int(order[i])-1]):
        s += str(p[int(order[i])-1] - count) + ' '
        count = p[int(order[i])-1]

    else:
        s += '0 '

print(s.rstrip())