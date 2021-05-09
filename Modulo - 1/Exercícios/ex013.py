salario = float(input('Digite seu salario: '))

novo = salario + (salario * 15 / 100)

print('Seu salario aumentou de R${} para R${:.2f} com 15% de aumento!'.format(salario, novo))
