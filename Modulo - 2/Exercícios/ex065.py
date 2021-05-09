maior = menor = media = cont = soma = 0
continuar = 'S'

while continuar == 'S':
    num = int(input('Informe um numero: '))
    soma += num
    cont += 1
    continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / cont
print('Voce digitou {} numeros e a media entre eles é igual a {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
