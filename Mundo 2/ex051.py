'''
Desenvolva um programa que leia o primeiros termo e a razão de uma PA. No final, mostre a soma
dos 10 primeiros termos dessa progressão.
'''

a1 = int(input('Digite o 1º termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
a10 = a1 + (10 - 1) * r
s10 = 0

for c in range(a1, a10 + r, r):
    print(c, end =' --> ')
    s10 += c

print(f'A soma dos termos da P.A. é: {s10 / 2}')





    