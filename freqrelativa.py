#valores instanciados
import statistics
frequencia = ([2,3,12,5,5,9,4])
total = 40
soma = 0
for c in range(0,7):
  j = frequencia[c] / total 
  k = j * 100
  soma += k
  print(k,'%')
print('A soma de todas as frequencias vai dar:',soma,'%')
