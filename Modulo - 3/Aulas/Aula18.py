# pessoas = [['Pedro', 15], ['Maria', 19], ['João', 32]]
# for pessoa in pessoas:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos.')

# --------------------------------------------------------

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# --------------------------------------------------------

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for pessoa in galera:
#     print(f'Nome: {pessoa[0]}... Idade: {pessoa[1]}')

# --------------------------------------------------------

# lista_pessoas = []
# dados_temporarios = []
# for contador in range(1, 4):
#     print('--' * 20)
#     print(f'DADOS DA {contador}° PESSOA')
#     print('--' * 20)
#     dados_temporarios.append(str(input('Digite seu nome: ')))
#     dados_temporarios.append(int(input('Digite sua idade: ')))
#     lista_pessoas.append(dados_temporarios[:])
#     dados_temporarios.clear()
# for pessoa in lista_pessoas:
#     if pessoa[1] >= 21:
#         print(f'{pessoa[0]} é maior de idade.')
#     else:
#         print(f'{pessoa[0]} é menor de idade.')
