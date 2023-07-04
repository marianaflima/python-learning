'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
c = 1
op = 10
total = 0

while op != 0:
    total += op
    while c <= total:
        print(f'{a1 + ((c - 1) * r)} --> ', end='')
        c += 1
    print('Pausa!')
    op = int(input('''
    Quantos termos a mais você quer ver (0 para sair)? '''))
print('FIM!')
