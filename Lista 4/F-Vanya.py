# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

x = 10**9 + 7
y = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'

s = input()
count = 0

for i in s:
    b = bin(int(y.find(i)))[2::]
    count += b.zfill(6).count('0')

print((3**count)%x)