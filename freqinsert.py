a = int(input("Quantos numeros vc vai colocar?:"))
lista = []
lista2 = []
lista3 = []
div = 0
soma = 0
for c in range(a):
  b = int(input("Digite os numeros:"))
  lista.append(b)
  div = div + (b/a)
  soma += b
lista2.append(soma)
lista3.append(div)
print('As frequencias sao: \n',lista,'\n A soma total das frequencias é:\n',lista2,'\n A media das frequencias é de:\n',lista3)
