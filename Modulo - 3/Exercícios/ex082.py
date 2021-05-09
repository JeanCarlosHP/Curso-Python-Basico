todos_valores = []
valores_impares = []
valores_pares = []
contador = 0
quer_continuar = 'S'
while True:
    contador += 1
    print('-' * 24)
    todos_valores.append(int(input(f'Digite o {contador}° valor: ')))
    quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while quer_continuar not in 'SN':
        quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
for valor in todos_valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
print('Todos os valores digitados: ', end='')
for todo_valor in todos_valores:
    print(todo_valor, end='... ')
print()
print('Todos os valores pares digitados: ', end='')
for valor_par in valores_pares:
    print(valor_par, end='... ')
print()
print('Todos os valores impares digitados: ', end='')
for valor_impar in valores_impares:
    print(valor_impar, end='... ')
print()
