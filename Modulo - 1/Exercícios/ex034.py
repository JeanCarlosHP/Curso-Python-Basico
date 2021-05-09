salario = float(input('Quanto voce ganha? '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu novo salario é {}'.format(novo))
