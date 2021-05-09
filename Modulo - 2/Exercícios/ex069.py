mais18 = maisHomens = menosMulheres = 0
cont = 1

while True:
    print('-=-' * 10)
    print(f'DADOS DA {cont}° PESSOA')
    print('-=-' * 10)

    idade = int(input(f'Informe a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Informe o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        maisHomens += 1
    if sexo == 'F' and idade < 20:
        menosMulheres += 1
    print()
    print('Dados registrados com sucesso!')
    print('---' * 10)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
    print()
    cont += 1

print('~' * 32)
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'{maisHomens} homens foram cadastrados.')
print(f'{menosMulheres} mulheres tem menos de 20 anos.')
print('~' * 32)
