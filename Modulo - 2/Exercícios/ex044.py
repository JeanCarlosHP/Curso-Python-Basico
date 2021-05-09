precoProduto = float(input('Informe o preço do produto: R$'))
print()

print('-' * 20)
print('[ 1 ] para: A vista dinheiro/cheque, 10% de desconto')
print('[ 2 ] para: A vista no cartão, 5% de desconto')
print('[ 3 ] para: Em até 2x no cartão, preço normal')
print('[ 4 ] para: 3x ou mais no cartão, 20% de juros')
print('-' * 20)
condicaoPagamento = int(input('Qual a condição de pagamento? '))

if condicaoPagamento == 1:
    desconto = precoProduto - ((precoProduto * 10) / 100)
    print('Agora o produto custa R${}'.format(desconto))
elif condicaoPagamento == 2:
    desconto = precoProduto - ((precoProduto * 5) / 100)
    print('Agora o produto custa R${}'.format(desconto))
elif condicaoPagamento == 3:
    print('O produto custa R${}'.format(precoProduto))
elif condicaoPagamento == 4:
    juros = ((precoProduto * 20) / 100) + precoProduto
    print('Agora o produto custa R${}'.format(juros))
else:
    print('Opção Inválida!')
