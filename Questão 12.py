num = []
op = 'S'
soma = n = 0
while op == 'S':
  num.append(int(input('Insira um numero-> ')))
  op = str(input('Inserir mais um?[S/N] ')).upper()[0]
for i in range(len(num)):
  if num[i] > 1:
    n = num[i]
    for j in range(2, n):
      if n % j == 0:
        num[i] = 0
        break
  for i in range(len(num)):
    soma += num[i]
print(f'A soma dos numeros primos inseridos é {soma}')