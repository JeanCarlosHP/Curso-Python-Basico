from random import randint
from time import sleep

num = randint(0, 5)

print('Vou pensar em um numero entre 0 e 5...')
adivinha = int(input('Adivinhe o numero que o computador pensou: '))
print('Estou processando...')
sleep(2)

if adivinha == num:
    print('Parabens! Voce acertou')
else:
    print('Que pena! Voce errou')
    print('O numero era... {}'.format(num))
