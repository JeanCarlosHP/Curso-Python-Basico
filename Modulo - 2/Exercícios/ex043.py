altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
print('Seu índice de massa corporal é igual há {:.1f}'.format(imc))

if imc < 18.5:
    print('Considerado abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Considerado peso ideal')
elif 25 <= imc <= 30:
    print('Considerado sobrepeso')
elif 30 <= imc <= 40:
    print('Considerado obesidade')
else:
    print('Considerado obesidade mórbida')
