dados_jogador = {}
quantidade_gols = []
soma = 0
dados_jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
quantidade_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
for contador in range(0, quantidade_partidas):
    quantidade_gols.append(int(input(f'Quantos gols na {contador + 1}° partida? ')))
contador = 0
for total in quantidade_gols:
    soma += total
dados_jogador['quantidade de gols'] = quantidade_gols[:]
dados_jogador['total'] = soma
print('-=-' * 20)
for key, value in dados_jogador.items():
    print(f'O campo {key} tem o valor {value}.')
print('-=-' * 20)
print(f'O jogador {dados_jogador["nome"]} jogou {quantidade_partidas} partidas.')
for partida in quantidade_gols:
    contador += 1
    print(f'    -> Na {contador}° partida, fez {partida} gols')
print(f'Foi um total de {dados_jogador["total"]} gols.')
