'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a função while
an = a1 + (n - 1) * r
'''
a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
n = 1
an = a1 + ((n - 1) * r)

print('(', end='')
while n <= 10:
    print(f'{a1 + ((n - 1) * r)}', end='')
    print(', ' if n < 10 else ')', end='')
    n += 1
    
    