from random import randint
from time import sleep
todos_jogos = []
jogos = []

total = 1
print('---' * 10)
print('{: ^30}'.format('JOGA NA MEGA SENA'))
print('---' * 10)

quantidade_sorteios = int(input('Quantos jogos voce quer que eu sorteie? '))
print()
while total <= quantidade_sorteios:
    contador = 0
    while True:
        valor_jogo = randint(1, 60)
        if valor_jogo not in todos_jogos:
            todos_jogos.append(valor_jogo)
            contador += 1
        if contador >= 6:
            break
    todos_jogos.sort()
    jogos.append(todos_jogos[:])
    todos_jogos.clear()
    total += 1
print(f'-=-=-=-=-=-=-=-= SORTEANDO {quantidade_sorteios} JOGOS =-=-=-=-=-=-=-=-')
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
print('-=-=-=-=-=-=-=-=-=-= BOA SORTE =-=-=-=-=-=-=-=-=-=-')
