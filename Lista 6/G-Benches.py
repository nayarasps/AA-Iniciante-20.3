# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

import math
 
n = int(input())
 
b1 = n**2
b2 = (n-1)**2
b3 = (n-2)**2
b4 = (n-3)**2
b5 = (n-4)**2
 
r = (b1*b2*b3*b4*b5)//math.factorial(5)
print(r)