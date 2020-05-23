#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

x = int(input("Numero:"))
def programa(x):
  if x > 0:
    print("P")
  else:
    print("N")
programa(x)
