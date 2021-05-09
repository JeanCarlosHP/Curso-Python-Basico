def mostraLinha(tamanho):
    print('-=-' * tamanho)


def moeda(preco=0):
    return f'R${preco:.2f}'.replace('.', ',')


def metade(preco, formatacao=False):
    metade_preco = preco / 2
    return metade_preco if not formatacao else moeda(metade_preco)


def dobro(preco=0, formatacao=False):
    dobro_preco = preco * 2
    return dobro_preco if not formatacao else moeda(dobro_preco)


def aumentar(preco, aumento=0, formatacao=False):
    preco = preco + (preco * aumento / 100)
    return preco if not formatacao else moeda(preco)


def diminuir(preco, diminui=0, formatacao=False):
    preco = preco - (preco * diminui / 100)
    return preco if not formatacao else moeda(preco)
