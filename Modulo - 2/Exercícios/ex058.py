from random import randint
from time import sleep

palpites = 1

num = randint(0, 10)
print('Vou pensar em um numero entre 0 e 10...')
adivinha = int(input('Adivinhe o numero que o computador pensou: '))
print()
print('Estou processando a resposta...')
print()
sleep(2)

print('-=-' * 25)
print()
if adivinha < num:
    print('Mais... Tente novamente!')
elif adivinha > num:
    print('Menos... Tente novamente!')
elif adivinha == num:
    print('Parabens! Voce acertou.')
if adivinha != num:
    while adivinha != num:
        palpites += 1
        adivinha = int(input('Adivinhe o numero que o computador pensou: '))
        print()
        print('Estou processando a resposta...')
        print()
        print('-=-' * 25)
        print()
        sleep(2)
        if adivinha < num:
            print('Mais... Tente novamente!')
        elif adivinha > num:
            print('Menos... Tente novamente!')
        else:
            print('Parabens! Voce acertou.')
print('Voce precisou de {} palpites para acertar'.format(palpites))
