def mostraLinha(tamanho):
    print('-=-' * tamanho)


def moeda(preco=0):
    preco = f'R${preco:.2f}'.replace('.', ',')
    return preco


def metade(preco=0):
    metade_preco = preco / 2
    return metade_preco


def dobro(preco=0):
    dobro_preco = preco * 2
    return dobro_preco


def aumentar(preco=0, aumento=0):
    preco = preco + (preco * aumento / 100)
    return preco


def diminuir(preco=0, diminui=0):
    preco = preco - (preco * diminui / 100)
    return preco
