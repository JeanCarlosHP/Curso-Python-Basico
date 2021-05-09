lista_numeros = []
for contador in range(0, 5):
    lista_numeros.append(int(input(f'Digite um valor para a posicao {contador}: ')))
print('-=-' * 15)
print('Voce digitou os valores: ', end='')
for valor in lista_numeros:
    print(valor, end=' ')
print()
maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)
print(f'O maior valor digitado foi {maior_valor} na posição ', end='')
for posicao, valor in enumerate(lista_numeros):
    if valor == maior_valor:
        print(posicao, end='... ')
print()
print(f'O menor valor digitado foi {menor_valor} na posição ', end='')
for posicao, valor in enumerate(lista_numeros):
    if valor == menor_valor:
        print(posicao, end='... ')
