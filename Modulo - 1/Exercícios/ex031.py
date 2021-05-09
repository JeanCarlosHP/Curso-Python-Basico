distancia = float(input("Digite a distancia da viagem em KM: "))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O valor da passagem é R${:.2f}'.format(passagem))
