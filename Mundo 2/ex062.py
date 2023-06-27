'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
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

op = int(input)
