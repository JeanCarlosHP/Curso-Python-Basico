def mostraLinha(tamanho):
    print('-=-' * tamanho)


def metade(preco):
    metade_preco = preco / 2
    return metade_preco


def dobro(preco):
    dobro_preco = preco * 2
    return dobro_preco


def aumentar(preco, aumento):
    preco = preco + (preco * aumento / 100)
    return preco


def diminuir(preco, diminui):
    preco = preco - (preco * diminui / 100)
    return preco
