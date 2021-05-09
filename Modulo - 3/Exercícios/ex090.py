dados_aluno = dict()
dados_aluno['Nome'] = str(input('Nome: ')).capitalize()
dados_aluno['Média'] = float(input(f'Média de {dados_aluno["Nome"]}: '))
if dados_aluno['Média'] >= 7:
    dados_aluno['Situação'] = 'Aprovado'
elif 5 <= dados_aluno['Média'] < 7:
    dados_aluno['Situação'] = 'Recuperação'
else:
    dados_aluno['Situação'] = 'Reprovado'
print('-=-' * 9)
for key, value in dados_aluno.items():
    print(f'{key} igual a {value}')
