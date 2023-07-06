'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será in-
terrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
'''
from random import randint
c = 0
cpu = 0
op_cpu = ''
soma = 0
winner = ''

print('-='*30)
print('         PAR OU ÍMPAR        ')
print('-='*30)



while True:
    op_player = str(input('Você vai de IMPAR ou PAR? ')).upper().split()
    while op_player[0][0] not in 'PI':
        op_player = str(input('Opção inválida! Você vai de IMPAR ou PAR? [P/I]')).upper().split()
        op_player = op_player[0][0]

    if op_player[0][0] == 'P':
        op_cpu = 'I'
    elif op_player[0][0] == 'I':
        op_cpu = 'P'
    
    cpu = randint(0,11)
    print('''
O computador pensou em um número''')
    player = int(input('Digite sua opção (entre 0 e 10): '))
    soma = cpu + player
    
    if op_player == 'P':
        if soma % 2 == 0:
            winner = 'Player!'
            c += 1
        else:
            winner = 'CPU!'
            break
    else:
        if soma % 2 != 0:
            winner = 'Player!'
            c += 1 
        else:
            winner = 'CPU!'
            break
    print(f'''
Vencedor: {winner}''')
    print(f'Opção da CPU: {cpu}')
    print(f'Opção do jogador: {player}')

print(f'''
Vencedor: {winner}''')
print(f'Opção da CPU: {cpu}')
print(f'Opção do jogador: {player}')


print(f'''
Vitórias consecutivas: {c}
''')