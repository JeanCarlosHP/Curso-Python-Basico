from ex108 import moeda108

preco = float(input('Digite o preço: R$'))
moeda108.mostraLinha(10)
print(f'A metade de {moeda108.moeda(preco)} é {moeda108.moeda(moeda108.metade(preco))}')
print(f'O dobro de {moeda108.moeda(preco)} é {moeda108.moeda(moeda108.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda108.moeda(moeda108.aumentar(preco, 10))}')
print(f'Reduzindo 13%, temos {moeda108.moeda(moeda108.diminuir(preco, 13))}')
moeda108.mostraLinha(10)
