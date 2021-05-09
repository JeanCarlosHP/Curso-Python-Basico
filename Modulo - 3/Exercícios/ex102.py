def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param numero: O numero a ser calculado.
    :param show: (opcional) mostra ou nao a equacao.
    :return: O valor do fatorial de (numero).
    """
    print('-' * 40)
    fat = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= contador
    return fat


print(fatorial(int(input('Fatorial de qual numero? ')), show=True))
print()
help(fatorial)
