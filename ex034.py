'''
Escreva um programa que pergunte o salário de um funcio-
nário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250.00, calcule um aumento
de 10%. Para inferiores ou iguais, o aumento é de 15%.
'''

sal = float(input('Digite seu salário (R$): '))

if sal <= 1250:
    sal *= 1.15
else:
    sal *= 1.1

print(f'Seu novo salário é: R$ {sal:.2f}')