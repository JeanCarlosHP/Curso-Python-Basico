a1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

for i in range(1, 11):
    print('{}º termo: {}'.format(i, a1))
    a1 += r
