'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o núme-
ro solicitado for negativo.
'''
n = int(input('Digite um número para ver sua tabuada: '))

while n > 0:
    print(f'TABUADA DE {n}')
    for i in range (1, 11):
        print(f'{n} x {i} = {n * i}')
    n = int(input('Digite um número para ver sua tabuada: '))