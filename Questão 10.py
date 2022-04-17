num = []
op = 'S'
soma = 0
while op == 'S':
  num.append(int(input('Insira um numero-> ')))
  op = str(input('Inserir mais um?[S/N] ')).upper()[0]
for i in num:
  if i%2 == 0:
    soma +=i
print(f'A soma dos valores pares é {soma}')