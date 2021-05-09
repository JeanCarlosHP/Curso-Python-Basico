"""
Crie um pacote chamado utilidadesCeV
que tenha dois módulos internos chamados moedas e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110
para o primeiro pacote e mantenha tudo funcionando.
"""
from ex111.utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 12)
