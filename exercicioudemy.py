x = [] #lista
cont = 0 #contador inicia em zero
for i in range(0,7): # for de 0 a 7 pra ser repetido 7 vezes
  x.append(float(input("Digita o peso:"))) # adicionando numeros na lista 
  if x[i] > 90: # se x na posicao I for maior que 90
    cont += 1 
print(cont,sum(x)/len(x)) # sum = somando todos os valores de x, len x = contador de x
