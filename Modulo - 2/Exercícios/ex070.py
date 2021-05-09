total = quantProdu = produtoMaisBarato = cont = 0
nomeProdutoMaisBarato = ''

while True:
    print('-=-' * 9)
    print(f'{cont}° PRODUTO')
    print('-=-' * 9)
    nome = ' '
    while nome == ' ':
        nome = str(input('Dado Invalido. Informe o nome do produto: ')).strip()
    preco = float(input('Informe o preco do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        quantProdu += 1
    if cont == 1 or preco < produtoMaisBarato:
        produtoMaisBarato = preco
        nomeProdutoMaisBarato = nome
    print()
    print('Produto Registrado!')
    print('--' * 10)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Dado Invalido. Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print()
print('~~~' * 19)
print(f'O total gasto na compra foi de R${total:.2f}.')
print(f'{quantProdu} produtos custam mais de R$1000.')
print(f'O nome do produto mais barato é {nomeProdutoMaisBarato} e custa R${produtoMaisBarato}.')
print('~~~' * 19)
