valorCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
quantidadeAnos = int(input('Informe a quantidade de anos que deseja pagar: '))

prestacaoMensal = valorCasa / (quantidadeAnos * 12)
porcentagemSalario = (salario * 30) / 100

if prestacaoMensal <= porcentagemSalario:
    print('Empréstimo aprovado!')
    print("Voce vai ter que pagar R${:.2f} de prestacao mensal".format(prestacaoMensal))
else:
    print('Empréstimo negado!')
