frase = str(input('Digite um frase: ')).replace(' ', '').lower()

fraseInvertida = frase[::-1]

if frase == fraseInvertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
print('O inverso de {} é {}'.format(frase, fraseInvertida))
