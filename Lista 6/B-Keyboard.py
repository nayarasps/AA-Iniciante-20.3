# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n, k = list(map(int, input().split()))

s = input()

a = input().split()

r = 0
count = 0
for i in range(n):
    if s[i] in a:
        count += 1
    else:
        r += count * (count + 1) // 2
        count = 0
r += count * (count + 1) // 2
print(r)