lista_numeros = []
quer_continuar = 'S'
while True:
    lista_numeros.append(int(input(f'Digite um valor: ')))
    quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while quer_continuar not in 'SN':
        quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
print(f'Voce digitou {len(lista_numeros)} elementos.')
lista_numeros.sort(reverse=True)
print('Os valores em ordem decrescente são: ', end='')
for valor in lista_numeros:
    print(valor, end='... ')
print()
if 5 in lista_numeros:
    print('O valor 5 faz parte da lista.', end=' ')
    print(f'E ele esta na posicao {lista_numeros.index(5)}')
else:
    print('O valor 5 não faz parte lista')
