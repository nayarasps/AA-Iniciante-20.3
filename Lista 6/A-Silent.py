# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())
 
d = {}
for i in range(n):
  a = input()

  if a[0] in d:
    d[a[0]] += 1
  else:
    d[a[0]] = 1
 
res = 0
for i,j in d.items():
  a = j//2
  b = j-a
  res += a * (a - 1) // 2;
  res += b * (b - 1) // 2;
 
print(res)