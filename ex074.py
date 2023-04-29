listagem = ('Frango', 3.5, 'Queijo', 5.00, 'Café', 0.5)

for i in range(0, len(listagem)):
    if (i % 2 == 0):
        print(f'{listagem[i]:.<20}')
    else:
        print(f'{listagem[i]:>8}')   

