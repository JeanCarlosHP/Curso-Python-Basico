todos_valores = []
for contador in range(1, 8):
    numero = int(input(f'Informe o {contador}° valor: '))
    todos_valores.append(numero)
todos_valores.sort()
print('-=-' * 15)
print(f'Os valores pares digitado foram: ', end='')
for valor in todos_valores:
    if valor % 2 == 0:
        print(valor, end=' ')
print()
print(f'Os valores impares digitado foram: ', end='')
for valor in todos_valores:
    if valor % 2 == 1:
        print(valor, end=' ')
