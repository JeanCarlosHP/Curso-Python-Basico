a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
cont = 1

while cont <= 10:
    print('{}º termo: {}'.format(cont, a1))
    a1 += r
    cont += 1
