from datetime import date

anoNascimento = int(input('Informe seu ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Mirim!')
elif idade <= 14:
    print('Infantil!')
elif idade <= 19:
    print('Junior!')
elif idade == 20:
    print('Senior!')
else:
    print('Master!')
