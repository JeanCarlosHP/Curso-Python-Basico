from random import randint

winLoss = parOuImpar = ' '
cont = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

while True:
    jogador = int(input('Diga um valor: '))
    compu = randint(1, 10)
    total = compu + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Impar [P/I]? ').strip().upper()[0]

    if escolha == 'P':
        if total % 2 == 0:
            winLoss = 'Voce Ganhou!'
            cont += 1
        else:
            parOuImpar = 'DEU IMPAR'
            winLoss = 'Voce Perdeu!'
            break
    elif escolha == 'I':
        if total % 2 == 1:
            winLoss = 'Voce Ganhou!'
            cont += 1
        else:
            parOuImpar = 'DEU PAR'
            winLoss = 'Voce Perdeu!'
            break

    print('-' * 22)
    print(winLoss)
    print('-' * 22)

print('---' * 20)
print(f'Voce jogou {jogador} e o computador {compu}. Total de {total} {parOuImpar}')
print(winLoss)
print(f'GAME OVER! Voce venceu {cont} vezes.')
print('---' * 20)
