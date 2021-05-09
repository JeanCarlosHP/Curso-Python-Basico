from math import sin, cos, tan, radians

angulo = float(input('Digite um angulo qualquer: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno do angulo {} é {:.2f}'.format(angulo, seno))
print('O cosseno do angulo {} é {:.2f}'.format(angulo, cosseno))
print('A tangente do angulo {} é {:.2f}'.format(angulo, tangente))
