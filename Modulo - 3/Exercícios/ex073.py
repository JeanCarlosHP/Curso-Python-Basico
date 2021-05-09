tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR', 'Sao Paulo', 'Internacional', 'Corinthians',
          'Fortaleza', 'Goias', 'Bahia', 'Vasco da Gama', 'Atletico-MG', 'Fluminense', 'Botafogo', 'Ceara SC',
          'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')

print('=-=' * 20)
print(f'Lista de times do brasileirao: {tabela}')
print('=-=' * 20)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('=-=' * 20)
print(f'Os 4 ultimos sao: {tabela[-4:]}')
print('=-=' * 20)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('=-=' * 20)

if 'Chapecoense' == tabela[-2]:
    print(f'O Chapecoense esta na {tabela.index("Chapecoense") + 1}ª posicao')
else:
    print('A Chapecoense nao foi classificada')
