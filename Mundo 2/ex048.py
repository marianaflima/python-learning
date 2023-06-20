'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos 
de três e que se encontram no intervalo de 1 até 500.
'''

for c in range(0, 501):
    if c % 3 == 0:
        s = s + c
print(f'A soma total é: {s}')