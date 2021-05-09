def mostraLinha(tamanho):
    print('-=-' * tamanho)


def moeda(preco=0):
    preco = f'R${preco:.2f}'.replace('.', ',')
    return preco


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


def resumo(preco, aumenta, diminui):
    mostraLinha(10)
    print('Resumo do valor'.center(30))
    mostraLinha(10)
    print(f'Preço analisado:{moeda(preco):>12}')
    print(f'Dobro do preço:{moeda(dobro(preco)):>14}')
    print(f'Metade do preço:{moeda(metade(preco)):>12}')
    print(f'{aumenta}% de aumento:{moeda(aumentar(preco, aumenta)):>13}')
    print(f'{diminui}% de redução:{moeda(diminuir(preco, diminui)):>13}')
    mostraLinha(10)
