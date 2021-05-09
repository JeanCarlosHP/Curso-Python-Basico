lista_notas = []


def notas(*valores, situacao=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param valores: Aceita várias notas.
    :param situacao: (Opcional) se vai ou não mostra a situção da média.
    :return: Quantidade de notas, maior e menor nota, média e a situação.
    """
    soma = 0
    for valor in valores:
        lista_notas.append(valor)
        soma += valor
    media = soma / len(lista_notas)
    print(f'Quantidade de notas: {len(lista_notas)}.')
    print(f'Maior nota: {max(lista_notas)}.')
    print(f'Menor nota: {min(lista_notas)}.')
    print(f'Média das notas: {media:.2f}.')
    if situacao:
        if 0 <= media <= 5:
            print('Situação: Ruim.')
        if 6 <= media < 7:
            print('Situação: Razoável.')
        if 7 <= media <= 8:
            print('Situação: Boa.')
        if 9 <= media <= 10:
            print('Situação: Exelente.')
    return lista_notas


notas(5.5, 2.5, 1.5, situacao=True)
print()
help(notas)
