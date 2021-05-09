km = float(input('Informe a quantidade de km rodados: '))
dias = int(input('Informe a quantidade de dias alugados: '))

total = (dias * 60) + (km * 0.15)

print('O valor de {} dias de aluguel deu R${} e dos km rodados ficou R${}, um total de R${}'.format(dias, diaria, valor_km_rodaddos, total))
