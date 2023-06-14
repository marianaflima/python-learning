'''
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar 
um triângulo.
'''
a = int(input('Digite um lado: '))
b = int(input('Digite outro lado: '))
c = int(input('Digite outro lado: '))

if a < b + c and b < a + c and c < a + b:
    print('Podem formar triângulo')
else:
    print('Não podem formar triângulo')