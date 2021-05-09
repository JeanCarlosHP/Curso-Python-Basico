lista_valores = []
for contador in range(0, 5):
    print('-' * 43)
    numero = int(input(f'Digite o valor da posicao {contador}: '))
    if contador == 0 or numero > lista_valores[-1]:
        lista_valores.append(numero)
        print('Valor adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista_valores):
            if numero <= lista_valores[posicao]:
                lista_valores.insert(posicao, numero)
                print(f'Valor adicionado na posicao {posicao}ª da lista...')
                break
            posicao += 1
print('-=-' * 16)
print('Os valores digitados em ordem foram: ', end='')
for valor in lista_valores:
    print(valor, end=' ')
print()
