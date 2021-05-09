lista_numeros = []
while True:
    valor = str(input('Digite um valor: '))
    if valor in lista_numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista_numeros.append(valor)
        print('Valor adicionado com sucesso...')
    quer_continuar = ' '
    while quer_continuar not in 'SN':
        quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
print('-=-' * 15)
print('Voce digitou os valores: ', end='')
lista_numeros.sort()
for valor in lista_numeros:
    print(valor, end=' ')
print()
