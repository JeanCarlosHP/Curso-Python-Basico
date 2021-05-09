from random import randint
from time import sleep
from operator import itemgetter
numeros_dado = {}
ranking = []
contador = 0
print('Valores Sorteados: ')
for jogador in range(1, 5):
    numeros_dado[f'jogador{jogador}'] = randint(1, 6)
for values in numeros_dado.items():
    contador += 1
    print(f'   O jogador{contador} tirou: {values[1]}')
    sleep(1)
ranking = sorted(numeros_dado.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for indice, value in enumerate(ranking):
    print(f'   {indice + 1}º lugar: {value[0]} com {value[1]}.')
    sleep(1)
