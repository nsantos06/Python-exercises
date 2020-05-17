#ler duas matrizes, os pares da Matriz A e impares da matriz B, adicionar na Matriz C



x = int(input("repetidor:"))
y = int(input("repetidor na 2 matriz"))
a=[]
b=[]
c=[]
for k in range(x):
  x1 = int(input("Numeros:"))
  a.append(x1)
  if x1 % 2 == 0:
    c.append(x1)
for j in range(y):
  x2 = int(input("Numeros na segunda matriz:"))
  b.append(x2)
  if x2 % 2 == 1:
    c.append(x2)

print(c)
