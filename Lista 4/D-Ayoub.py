# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

x = 10**9 + 7

n,l,r = list(map(int, input().split()))

a = r//3-(l-1)//3
b = (r+2)//3-(l+1)//3
c = (r+1)//3-(l)//3
    
y = 1
w = 0
z = 0

for i in range(n):
    k = (y*a+w*c+z*b)%x
    j = (y*b+w*a+z*c)%x
    l = (y*c+w*b+z*a)%x
    
    y,w,z = k,j,l

print(y)