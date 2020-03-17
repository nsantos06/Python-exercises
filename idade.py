
#Fazer um algoritmo que lia um numero inderteminado de linhas contendo cada uma a idade de um individuo
#A ultima linha que não entrará nos calculos contem o valor da idade igual a zero.
#Calcula e imprima a idade média deste grupo de individuos
n = 0
k = int(input("qnts vezes vai repetir :"))
for c in range(0,k):
  idade = int(input("Digite a idade:"))
  if (k-1) != c:
    n = n + idade

media = n/(k-1)
print(media)
