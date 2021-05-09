parenteses_aberto = parenteses_fechado = 0
print('---' * 10)
expressao = str(input('Digite a expressão: '))
print('---' * 10)
expressao_separada = [expressao.join(' ')]
for parenteses in expressao:
    if parenteses == '(':
        parenteses_aberto += 1
    if parenteses == ')':
        parenteses_fechado += 1
if parenteses_aberto == parenteses_fechado:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
