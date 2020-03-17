#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
soma = []
multi = []
n = 0
a = 1
for c in range(5):
  k = int(input("Digite os 5 numeros:"))
  n = k+k
  soma.append(n)
  a = k*k
  multi.append(a)
  numeros.append(k)
print(f'Numeros:{numeros}, \n Soma{soma}, \n Multi{multi}')
