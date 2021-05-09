dados_temporarios = {}
acima_da_media = {}
dados_pessoas = []
mulheres = []
soma = 0
while True:
    dados_temporarios['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dados_temporarios['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados_temporarios['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados_temporarios['idade'] = int(input('Idade: '))
    soma += dados_temporarios['idade']
    if dados_temporarios['sexo'] == 'F':
        mulheres.append(dados_temporarios['nome'])
    acima_da_media = dados_temporarios.copy()
    dados_pessoas.append(dados_temporarios.copy())
    dados_temporarios.clear()
    while True:
        quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if quer_continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if quer_continuar == 'N':
        break
    print('-=-' * 9)
media = soma / len(dados_pessoas)
print('-~-' * 16)
print(f'- O grupo tem {len(dados_pessoas)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for nome in mulheres:
    print(nome, end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for pessoa in dados_pessoas:
    if pessoa['idade'] > media:
        for key, value in pessoa.items():
            print(f'{key} = {value}', end='; ')
    print()
print()
print('<<< ENCERRADO >>>')
