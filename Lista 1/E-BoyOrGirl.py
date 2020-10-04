# @author Nayara Souza
# UFCG - Universidade Federal de Campina Grande
# AA - Basico

entrada = input()
letras = "".join(set(entrada))

if len(letras) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
