from ex107 import moeda107

preco = float(input('Digite o preço: R$'))
moeda107.mostraLinha(10)
print(f'A metade de {preco} é {moeda107.metade(preco)}')
print(f'O dobro de {preco} é {moeda107.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda107.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {moeda107.diminuir(preco, 13)}')
moeda107.mostraLinha(10)
