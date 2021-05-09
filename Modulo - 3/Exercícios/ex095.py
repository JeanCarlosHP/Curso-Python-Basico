dados_jogadores = []
dados_temporarios = {}
quantidade_de_gols = []
contador = 0
soma = 0
while True:
    nome = str(input('Nome do jogador: ')).capitalize()
    quantidade_partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for gols in range(0, quantidade_partidas):
        contador += 1
        quantidade_de_gols.append(int(input(f'Quantos gols na {contador}° partida? ')))
    contador = 0
    for total in quantidade_de_gols:
        soma += total
    dados_temporarios['nome'] = nome
    dados_temporarios['quantidade de gols'] = quantidade_de_gols[:]
    dados_temporarios['total'] = soma
    dados_jogadores.append(dados_temporarios.copy())
    soma = 0
    quantidade_de_gols.clear()
    dados_temporarios.clear()
    quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while quer_continuar not in 'SN':
        quer_continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
    print('-=-' * 10)
print('-=-' * 20)
print(f'{"cod  nome"}{"gols":>15}{"total":>15}')
print('---' * 16)
for keys, value in enumerate(dados_jogadores):
    print(f'{keys:>1}   ', end=' ')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
print('---' * 16)
while True:
    buscar_jogador = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if buscar_jogador == 999:
        break
    if buscar_jogador >= len(dados_jogadores):
        print(f'ERRO! Não existe jogador com código {buscar_jogador}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {dados_jogadores[buscar_jogador]["nome"]}:')
        for indice, gols in enumerate(dados_jogadores[buscar_jogador]['gols']):
            print(f'    No jogo {indice + 1} fez {gols} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
