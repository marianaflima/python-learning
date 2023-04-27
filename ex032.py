'''
Faça um programa que leia um ano e mostre se ele é
ano bissexto
'''

ano = int(input('Digite um ano: '))

if (ano % 4 == 0) or (ano % 400 == 0):
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto')
