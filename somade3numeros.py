#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

x = int(input("Numero 1 :"))
y = int(input("Numero 2 :"))
z = int(input("Numero 3 :"))
def soma(x,y,z):
  resultado = x+y+z
  print("O resultado é:",resultado)
soma(x,y,z)
