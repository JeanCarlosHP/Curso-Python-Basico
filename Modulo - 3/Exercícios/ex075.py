cont = 0
num = (int(input(f'Digite o 1° valor: ')), int(input(f'Digite o 2° valor: ')),
       int(input(f'Digite o 3° valor: ')), int(input(f'Digite o 4° valor: ')))
print('-' * 40)
print('Voce digitou os valores: ', end='')
for n in num:
    print(n, end=' ')
print()
print('-' * 40)
if num.count(9) > 0:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
else:
    print('Nenhum valor 9 digitado.')
print('-' * 40)
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posicao.')
else:
    print('Nenhum valor 3 digitado.')
print('-' * 40)
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
        cont += 1
    if cont == 0:
        print('Nenhum valor par digitado.')
print()
print('-' * 40)
