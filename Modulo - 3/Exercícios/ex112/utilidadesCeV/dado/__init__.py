def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        preco = str(input(mensagem)).strip().replace(',', '.')
        if preco.isalpha() or preco == '':
            print(f'ERRO! "{preco}" é um preço inválido!')
        else:
            valido = True
            return float(preco)
