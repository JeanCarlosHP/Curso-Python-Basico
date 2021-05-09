from random import choice
from time import sleep

print('[ Pedra ]')
print('[ Papel ]')
print('[ Tesoura ] ')

jogador = input('Qual vai ser sua jogada? ')
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)
print()

print('Pedra...')
sleep(0.7)
print('Papel...')
sleep(0.7)
print('Tesoura...')
print()

print('-=-' * 20)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-=-' * 20)
print()

if jogador == 'Papel' and computador == 'Pedra':
    print('Jogador venceu!')
elif jogador == 'Pedra' and computador == 'Papel':
    print('Computador venceu!')
elif jogador == 'Pedra' and computador == 'Pedra':
    print('Empate!')
elif jogador == 'Pedra' and computador == 'Tesoura':
    print('Jogador venceu!')
elif jogador == 'Tesoura' and computador == 'Pedra':
    print('Computador venceu!')
elif jogador == 'Papel' and computador == 'Papel':
    print('Empate!')
elif jogador == 'Tesoura' and computador == 'Papel':
    print('Jogador venceu!')
elif jogador == 'Papel' and computador == 'Tesoura':
    print('Computador venceu!')
elif jogador == 'Tesoura' and computador == 'Tesoura':
    print('Empate!')
