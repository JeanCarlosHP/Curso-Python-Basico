from random import randint
from time import sleep
lista_numeros = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for valores in range(0, 5):
        valor = randint(1, 10)
        print(valor, end=' ')
        lista_numeros.append(valor)
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    soma = 0
    print('Somando os valores pares de [ ', end='')
    for valor in lista_numeros:
        print(valor, end=' ')
        if valor % 2 == 0:
            soma += valor
    print(f'], temos {soma}.')


sorteia()
somaPar()
