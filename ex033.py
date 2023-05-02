'''
Faça um programa que leia três números e mostre qual é
o maior e qual é o menor.
'''
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

Maior = a
if b>a and b>c:
    Maior = b
if c>a and b>c:
    Maior = c

Menor = c
if b<a and b<c:
    Menor = b
if a<b and a<c:
    Menor = a

    

print(f'Maior número: {Maior} \n Menor número: {Menor}')