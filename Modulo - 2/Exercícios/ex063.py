num = int(input('Informe um numero inteiro: '))
cont = 3
termo1 = 0
termo2 = 1
print('{} ➜ {}'.format(termo1, termo2), end='')

while cont <= num:
    termo3 = termo1 + termo2
    print(' ➜ {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' ➜ Fim!')
