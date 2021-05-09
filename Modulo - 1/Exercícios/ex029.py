speed = int(input('Digite a velocidade do carro: '))

if speed > 80:
    valorMulta = (speed - 80) * 7
    print('Voce foi multado! O valor da multa é R${},00'.format(valorMulta))
print('Voce nao foi multado!')
