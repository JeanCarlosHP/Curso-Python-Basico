from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    anoNascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1

if menor == 1:
    print('{} pessoa é menor de idade'.format(menor))
else:
    print('{} pessoas são menores de idade'.format(menor))

if maior == 1:
    print('{} pessoa é maior de idade'.format(maior))
else:
    print('{} pessoas são maiores de idade'.format(maior))
