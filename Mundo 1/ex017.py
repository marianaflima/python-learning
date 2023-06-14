from math import hypot as hip

a = float(input('Digite o valor do 1º cateto: '))
b = float(input('Digite o valor do 2º cateto: '))

print(f'O resultado da hipotenusa de {a} e {b} é {hip(a, b)}')