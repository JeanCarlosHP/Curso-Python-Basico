def ficha(nome, gols):
    print('--' * 20)
    if nome == '':
        nome = '<desconhecido>'
    if gols not in '0123456789':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('--' * 20)
ficha(nome=str(input('Nome do jogador: ')), gols=str(input('Numero de gols: ')))
