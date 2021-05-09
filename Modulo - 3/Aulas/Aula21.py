# help(print)
#
#
# def contador(i, f, p):
#     """
#     Faz um contagem e mostra na tela
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(c, end=' ')
#         c += 1
#     print('FIM!')


# ---------------------------------------------

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(s)
#
#
# somar(3, 2, 5)
# somar(8, 4)

# ---------------------------------------------

# def teste():
#     x = 8
#     print(f'Na funcao teste, n vale {n}')
#     print(f'Na funcao teste, x vale {x}')
#
#
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}')

# ---------------------------------------------


# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1}')
#
#
# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}')


# ---------------------------------------------


# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')


# ---------------------------------------------


# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# resposta1 = somar(3, 2, 5)
# resposta2 = somar(8, 4)
# print(f'Meus calculos deram {resposta1} e {resposta2}')


# ---------------------------------------------


# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# n = int(input('Digite um numero: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')

# ---------------------------------------------

# def par_ou_impar(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# num = int(input('Digite um numero: '))
# print(par_ou_impar(num))
# if par_ou_impar(num):
#     print('É Par!')
# else:
#     print('É Impar')
