num = []
seq = x = y = soma1 = soma2 = soma3 =0
while seq <= 10:
  seq = int(input('Digite o tamanho da Sequencia (maior que 10): '))
  if seq <= 10:
    print('Numero menor que 10')
while x == y or x < 2 or seq < x or y < 2 or seq < y:
  x = int(input('Digite o valor de X: '))
  y = int(input('Digite o valor de Y: '))
  if x == y:
    print('Numero iguais!\nDigite numeros diferentes\n')
  elif x < 2 or seq < x or y < 2 or seq < y:
    print('Numeros fora do tamanho da sequencia!\nDigite numeros entre 2 e o tamanho da sequencia\n')

for i in range(0, seq):
  num.append(int(input(f'Digite o {i+1} termo: ')))

for i in range(0, x):
  soma1 += num[i]
for i in range(x, y):
  soma2 += num[i]
for i in range(y, len(num)):
  soma3 += num[i]

print('Subconjunto em ordem crescente de acordo com a soma dos valores: ')
if soma1 > soma2 and soma1 > soma3:
  print(f'{num[:x]}')
  if soma2 > soma3:
    print(f'{num[x:y]}')
    print(f'{num[y:]}')
  else:
    print(f'{num[y:]}')
    print(f'{num[x:y]}')
elif soma2 > soma1 and soma2 > soma3:
  print(f'{num[x:y]}')
  if soma1 > soma3:
    print(f'{num[:x]}')
    print(f'{num[y:]}')
  else:
    print(f'{num[y:]}')
    print(f'{num[:x]}')
elif soma3 > soma1 and soma3 > soma2:
  print(f'{num[y:]}')
  if soma2 > soma1:
    print(f'{num[x:y]}')
    print(f'{num[:x]}')
  else:
    print(f'{num[:x]}')
    print(f'{num[x:y]}')
#print(f'[{soma1}] [{soma2}] [{soma3}]')