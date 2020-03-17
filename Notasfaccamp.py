#calcular as notas de forma "automatizada"
import math

#nota dos pbl
pbl1 = float(input("digita sua primeira nota do pbl: "))
pbl2 = float(input("digite a segunda nota do pbl: "))
x = (pbl1 + pbl2)/2
print("A sua media dos pbls é:",x)

#nota das provas
p1 = float(input("digita a primeira nota das provas: "))
p2 = float(input("digita a segunda nota das provas: "))
y = (p1 + p2)/2
print("A sua média das provas sao:",y)

#o resultado dos pbls multiplicado o resultado das notas
xy = x * y
xy1 = math.sqrt(xy)
print("A sua média total é:",xy1)
if xy1 >= 5:
  print("Parabéns você está aprovado nesta matéria")
else:
  print("Errrooou você nao está aprovado nesta matéria")
#edited in 24/06 2:52 PM
