#Faça um Programa que peça a idade e a altura de 5 pessoas, 
#armazene cada informação no seu respectivo vetor. 
#Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []
for c in range(5):
  age = int(input("Idade:"))
  height = str(input("Altura:"))
  idade.append(age)
  altura.append(height)
print(f'Idade:{idade[::-1]}, \n Altura:{altura[::-1]}')
