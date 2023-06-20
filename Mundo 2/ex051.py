'''
Desenvolva um programa que leia o primeiros termo e a razão de uma PA. No final, mostre a soma
dos 10 primeiros termos dessa progressão.
'''

a1 = int(input('Digite o 1º termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
s10 = 0
ac = 0

for c in range(1, 11):
    ac = a1 + ((c - 1)*r)
    s10 += ac

s10 /= 2

print(s10)


    