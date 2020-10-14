# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

n = int(input())

r = [0]*3

print("?",1,2)
x = int(input())

print("?",1,3)
y = int(input())

print("?",2,3)
z = int(input())

r[1]=((x+z)-y)//2
r[0]=x-r[1]
r[2]=y-r[0]

for i in range(4,n+1):
     print('?',i-1,i)
     x = int(input())
     r.append(x-r[i-2])
print('! ' + ' '.join(map(str,r)))