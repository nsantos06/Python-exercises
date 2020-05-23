#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

custo = float(input("Digite o custo:"))
taxaImposto = float(input("Digite a porcentagem de imposto:"))

def somaImposto(taxaImposto,custo):
  porcentagem = taxaImposto / 100
  conta = custo * porcentagem 
  valor = custo + conta
  print(valor)
somaImposto(taxaImposto,custo)
