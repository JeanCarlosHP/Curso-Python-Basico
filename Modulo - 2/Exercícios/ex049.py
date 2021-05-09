n = int(input('Quer a tabuada de qual número? '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n * i))
