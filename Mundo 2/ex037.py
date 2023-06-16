lista = (1, 2, 3)
num = int(input('Digite um número: '))
n_base = int(input('''
Para qual base será convertido?
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
'''))

if n_base not in lista:
    print('ERRO! Digite opções disponíveis.')
elif n_base == lista[0]:
    print(f'BINÁRIO: {(bin(num)[2:].upper())}')
elif n_base == lista[1]:
    print(f'OCTAL: {oct(num)[2:].upper()}')
elif n_base == lista[2]:
    print(f'HEXADECIMAL: {hex(num)[2:].upper()}')
