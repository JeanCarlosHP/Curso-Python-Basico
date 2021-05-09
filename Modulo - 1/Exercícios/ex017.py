from math import hypot

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hip = hypot(catetoOposto, catetoAdjacente)

print('O valor da hipotenusa é: {:.2f}'.format(hip))
