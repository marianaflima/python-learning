'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu progresso deverá realizar a operação em cada caso
'''
from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro valor: '))
op = 0

while op != 5:
    sleep(1.5)
    op = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
DIGITE SUA OPÇÃO: '''))
    if op == 1:
        print(f'A soma de {n1} e {n2} é: {n1 + n2}')
    elif op == 2:
        print(f'O produto de {n1} e {n2} é: {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif op == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))


if op == 5:
    print('SAINDO DO PROGRAMA...')