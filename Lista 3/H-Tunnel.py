# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

e = list(map(int,input().split()))
s = list(map(int,input().split()))


j = 0
i = 0
count = 0
f = set()

while len(f) < n:
    if e[i] == s[j]:
        f.add(s[j])
        j += 1
        i += 1
    elif e[i] != s[j] and e[i] not in f:
        count += 1
        f.add(s[j])
        j += 1
    else:
        i += 1


print(count)