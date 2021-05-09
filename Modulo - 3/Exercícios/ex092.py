from datetime import date
dados_pessoa = {}
ano_atual = date.today().year
nome = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))
dados_pessoa['nome'] = nome
dados_pessoa['idade'] = ano_atual - ano_de_nascimento
dados_pessoa['ctps'] = ctps
if ctps != 0:
    dados_pessoa['ano de contratacao'] = int(input('Ano de contratação: '))
    dados_pessoa['salario'] = float(input('Salário: R$ '))
    dados_pessoa['aposentadoria'] = dados_pessoa['idade'] + ((dados_pessoa[' ano de contratacao'] + 35) - ano_atual)
for key, value in dados_pessoa.items():
    print(f'- {key} tem o valor {value}')
