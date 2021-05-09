lista_pessoas = []
lista_temporaria = []
maior_peso = menor_peso = 0
while True:
    print('--' * 15)
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso: ')))
    if len(lista_pessoas) == 0:
        maior_peso = menor_peso = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior_peso:
            maior_peso = lista_temporaria[1]
        if lista_temporaria[1] < menor_peso:
            menor_peso = lista_temporaria[1]
    lista_pessoas.append(lista_temporaria[:])
    lista_temporaria.clear()
    quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while quer_continuar not in 'SN':
        quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
print('-=-' * 20)
print(f'Ao todo, voce cadastrou {len(lista_pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}kg. Peso de ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        print(pessoa[0], end='... ')
print()
print(f'O menor peso foi de {menor_peso}kg. Peso de ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(pessoa[0], end='... ')
print()
print('-=-' * 20)
