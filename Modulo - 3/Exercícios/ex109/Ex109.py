from ex109 import moeda109

preco = float(input('Digite o preço: R$'))
moeda109.mostraLinha(10)
print(f'A metade de {moeda109.moeda(preco)} é {moeda109.metade(preco, True)}')
print(f'O dobro de {moeda109.moeda(preco)} é {moeda109.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda109.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda109.diminuir(preco, 13, True)}')
moeda109.mostraLinha(10)
