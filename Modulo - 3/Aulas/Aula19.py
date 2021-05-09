# dados = {'nome': 'Jean', 'idade': 17}
# print(f'Olá meu nome é {dados["nome"]} e tenho {dados["idade"]} anos')
# dados['sexo'] = 'M'
# print(dados['sexo'])
# del dados['sexo']

# -----------------------------------------------------------------------------

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'Idade': 22}
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5
# # print(pessoas['nome'])
# # print(pessoas.keys())
# # print(pessoas.values())
# # print(pessoas.items())
# for k, v in pessoas.items():
#     print(k, v)

# -----------------------------------------------------------------------------

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Sao Paula', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(brasil[0]['uf'])

# -----------------------------------------------------------------------------

# estado = {}
# brasil = []
# for contador in range(0, 3):
#     estado['uf'] = str(input('Unidadade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for estado in brasil:
#     for keys, values in estado.items():
#         print(f'{keys}: {values}')
