# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

mod = 10**9 + 7

s = input()
 
def getMod(x):
  return ((x % mod) + mod) % mod
 
r = 1
count = 1
 
for i in range(len(s)):
  if s[i] == "a":
    count += 1
  elif s[i] == "b":
    r = getMod(r*count)
    count = 1

r = getMod(getMod(r*count)-1)

print(r)
