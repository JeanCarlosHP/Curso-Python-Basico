r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triangulo!')
    if r1 == r2 == r3:
        print('Forma um triangulo equilatero!')
    elif r1 != r2 != r3 != r1:
        print('Forma um triangulo escaleno!')
    else:
        print('Forma um triangulo isoceles!')
else:
    print('Não forma um triangulo!')
