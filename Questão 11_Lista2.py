num = []
op = 'S'
soma = 0
while op == 'S':
  num.append(int(input('Insira um numero-> ')))
  op = str(input('Inserir mais um?[S/N] ')).upper()[0]
for i in range(len(num)):
  if num[i] > num[i-1]:
    soma += num[i]
  print(f'{i}, {soma}')
print(f'A soma dos valores maiores que seu predecessor é {soma+num[0]}')
