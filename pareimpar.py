#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

inteiro = []
par = []
impar = []
for c in range(20):
  k = int(input("Numeros:"))
  if k % 2 == 0:
    par.append(k)
  elif k % 2 == 1:
    impar.append(k)
    
  inteiro.append(k) 
print(f'Inteiros: {inteiro}, \n Pares:{par}, \n Impares:{impar}.')
