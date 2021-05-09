def titulo(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)


def ajuda():
    from time import sleep
    while True:
        titulo('Sistema de Ajuda PyHelp')
        sleep(1)
        comando = str(input('Função ou Biblioteca -> '))
        if comando.upper() == 'FIM':
            print('~' * 18)
            print(f'{"-- ATÉ LOGO --":^18}')
            print('~' * 18)
            sleep(1)
            break
        titulo(f'Acessando o manual do comando {comando}')
        print()
        sleep(1)
        help(comando)


ajuda()
